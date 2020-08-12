import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.png',0)
edges = cv2.Canny(img,100,200)
cv2.imshow("image", np.float32(edges))
cv2.imwrite("part2.png",np.float32(edges))
cv2.waitKey(0)