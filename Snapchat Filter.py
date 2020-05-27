
import cv2

# C:\Users\Cossette\Desktop
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# face = cv2.CascadeClassifier('C:/Users/Cossette/Desktop/haarcascade_mcs_leftear.xml')
# hat=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/hat.png')
glass=cv2.imread("C:/Users/Cossette/Desktop/Accessories/Earrings/Earring1.png")
# dog=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/dog.png')
def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.8 * face_height) + 1

    glass = cv2.resize(glass, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(-0.7* face_height)][x + j][k] = glass[i][j][k]
    return fc

webcam = cv2.VideoCapture(0)
while True:
    size=4
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray,1.19,7)

    for (x, y, w, h) in fl:

        im = put_glass(glass, im, x, y, w, h)

    cv2.imshow('Hat & glasses',im)
    key = cv2.waitKey(30) & 0xff
    if key == 27:  # The Esc key
       break