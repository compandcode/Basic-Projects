#Cartoon
import cv2

img = cv2.imread("IMG2.jpg") #Loads the image.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts from RGB to GrayScale.
gray = cv2.medianBlur(gray, 5) #Applies a blur.
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250) #Smoothens image and preserves edges.
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img) #Outputs the original image.
cv2.imshow("edges", edges) #Outputs the edges of the image.
cv2.imshow("Cartoon", cartoon) #Outputs the complete Cartoon image.
cv2.waitKey(0)
cv2.destroyAllWindows()

print("SUCCESS")

#Dimensions 1280*720 recommended!
