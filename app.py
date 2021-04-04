from flask import Flask, redirect, request, render_template, send_file
from PIL import Image
import face_recognition
from io import BytesIO

# Get the centroids
def centroid(vertexes):
    _x_list = [vertex [0] for vertex in vertexes]
    _y_list = [vertex [1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return(_x, _y)

def serve_pil_image(pil_img, pil_format, pil_mimetype):
    img_io = BytesIO()
    pil_img.save(img_io, pil_format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype=pil_mimetype)

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        pilOrigFoto = Image.open(request.files['foto'].stream)

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(request.files['foto'])

        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        # Create a PIL imagedraw object so we can draw on the picture
        pil_image = Image.fromarray(image)

        # Laser A
        laserA = Image.open("LaserA.png")
        rightEyeCenter = centroid(face_landmarks_list[0]['right_eye'])
        rightEyeCenterInt = (int(rightEyeCenter[0])-600,int(rightEyeCenter[1])-337)
        pil_image.paste(laserA, rightEyeCenterInt, laserA)
        leftEyeCenter = centroid(face_landmarks_list[0]['left_eye'])
        leftEyeCenterInt = (int(leftEyeCenter[0])-600,int(leftEyeCenter[1])-337)
        pil_image.paste(laserA, leftEyeCenterInt, laserA)

        return serve_pil_image(pil_image, pilOrigFoto.format, pilOrigFoto.get_format_mimetype())

    else:
        return render_template('index.html')

app.run(host='0.0.0.0', port=8181)
