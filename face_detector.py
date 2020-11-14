#Using haarcascade xml file for face detection
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")

#scaleFactor, with each iteration it will decrease the image size by
#0.05 and check the entirety of the image for a face 
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h in faces:
    #drawing a rectangle on the img, starting at x,y and the other coordinate is the diagonal
    #across point. Next is the color of the rectable (b,g,r) and the width of the line
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)

#will return an array
#1st value: column(x), 2nd: row(y), 3rd x 4th: dimensions of image surrounding face
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("photo", resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()

