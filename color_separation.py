import cv2
import numpy as np

#Working from "OpenCV for Python Developers"

img = cv2.imread("./Exercises/Ch02/02_04 Begin/butterfly.jpg", 1)
# Loads image as a numpy.ndarray, with preprocessing determined by the flag
# Image is an array row->pixel in row->channel in pixel
# Channels for this are blue, green, red - there can also be a fourth channel, which is transparency of that pixel
#Note that Python openCV's native image viewer doesn't support transparency
# Be careful! Different images can have different formats
height, width, channels = img.shape

print(f"Height: {height}, Width: {width}, Channels: {channels}")

#cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.moveWindow("Image", 0, 0)

b, g, r = cv2.split(img)
#Split image by color - produces 3 grayscale images corresponding to the blue, green and red intensities

#Inefficient numpy array concatenation
rgb_split = np.empty([height, width*3, channels], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width*2] = cv2.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv2.merge([r, r, r])

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convert from BGR (blue, green, red) to HSV (hue, saturation, value), i.e. color, satuation, luminosity
#HSV space can be more efficient than RGB space for recognizing color blobs
h, s, v = cv2.split(hsv)

#Efficient numpy array concatenation
hsv_split = np.concatenate((h, s, v), axis=1)

cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0) # Wait until key is pressed, function returns the number of the pressed key
cv2.destroyAllWindows()

#cv2.imwrite("./Outputs/output.jpg", img)