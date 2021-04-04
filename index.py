from PIL import Image
import face_recognition

# Get the centroids
def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     return(_x, _y)

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("./IMG_5960.png")

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
pil_image.show()
