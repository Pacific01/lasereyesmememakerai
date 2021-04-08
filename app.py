from PIL import Image, ExifTags
from flask import Flask, redirect, request, render_template, send_file
from io import BytesIO
from math import sqrt
import face_recognition
import numpy as np
import random

# HELPERS
# app.logger.info()

# Get the centroids
def centroid(vertexes):
    _x_list = [vertex [0] for vertex in vertexes]
    _y_list = [vertex [1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return(_x, _y)

def distance(A, B):
    return sqrt( (A[0] - B[0])**2 + (A[1] - B[1])**2 )

def serve_pil_image(pil_img, pil_format, pil_mimetype):
    img_io = BytesIO()
    pil_img.save(img_io, pil_format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype=pil_mimetype, as_attachment=True,
            attachment_filename='laserized.' + str.lower(pil_format))

def exifUp(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break

        exif = image._getexif()

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    return image

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Convert image into PIL image
        pilOrigFoto = Image.open(request.files['foto'].stream)

        # Straighten the image - Mobiles sometimes put images sideways
        image = exifUp(pilOrigFoto)

        # Load the jpg file into a numpy
        image = np.array(image.convert('RGB'))

        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        if len(face_landmarks_list) == 0:
            return render_template('index.html', errors=True)

        # landmaks
        A, B, C, D, E, F = face_landmarks_list[0]['right_eye']

        # Create a PIL imagedraw object so we can draw on the picture
        pil_image = Image.fromarray(image)

        # Laser Image
        color = random.choice(['Blue', 'Yellow', 'Green', 'Orange'])
        laserImage = Image.open("Laser"+color+".png")

        # Centroids
        rightEyeCenter = centroid(face_landmarks_list[0]['right_eye'])
        leftEyeCenter = centroid(face_landmarks_list[0]['left_eye'])

        # Resixe laser
        distanceBetweenEyes = distance(rightEyeCenter, leftEyeCenter)
        ratio = distance(A, D)/53 # 45 px para el LaserA

        # Resize Laser image
        laserImage = laserImage.resize((int(1200*ratio), int(674*ratio)))

        # Right Laser
        rightEyeCenterInt = (int(rightEyeCenter[0]-600*ratio),int(rightEyeCenter[1]-337*ratio))
        pil_image.paste(laserImage, rightEyeCenterInt, laserImage)

        # Left Laser
        leftEyeCenterInt = (int(leftEyeCenter[0]-600*ratio),int(leftEyeCenter[1]-337*ratio))
        pil_image.paste(laserImage, leftEyeCenterInt, laserImage)

        return serve_pil_image(pil_image, pilOrigFoto.format, pilOrigFoto.get_format_mimetype())

    else:
        return render_template('index.html')

app.run(host='0.0.0.0', port=8181)
