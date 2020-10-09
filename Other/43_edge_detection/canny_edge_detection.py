import cv2
import numpy as np

#additional library to be imported particularly for Google Colab
#as it doesn't support cv2.imshow() function
from google.colab.patches import cv2_imshow

#code to read the input image
img = cv2.imread('dinesh_pic.jpg')

#canny edge filter(kernel) for edge detection has been applied to the input image
canny = cv2.Canny(img,100,200)
#here aperture of the kernel has a min size of 100 and a max size of 200

#code to show the input image
cv2_imshow(img)

#code to show the output image with the detected edges of the input image
cv2_imshow(canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

