#library from openCV (computer vision)
import cv2

#one reads in the image with color, 0 would be grayscale, -1 would be color with 
#alpha (alpha would control transparency)
img = cv2.imread("galaxy.jpg", 0)

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(500)
#cv2.destroyAllWindows()

'''
#For importing a group of images 
import glob
images = glob.glob("*.jpg")
for image in images:
    img = cv2.imread(image, 0)
    resized_image = cv2.resize(img, (100,100))
    cv2.imwrite("resized_"+image, resized_image)
'''











