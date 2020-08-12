import cv2
import numpy as np

import math


   

def createFilter(sigma, kernelSize):

    kernel = np.zeros((kernelSize, kernelSize))
    s = 2 * (sigma * sigma)

    for i in range(kernelSize):
        for j in range(kernelSize):
            r = math.sqrt(i ** 2 + j ** 2)
            kernel[i, j] = (math.exp(-(r * r) / s)) / (3.14 * s)

    kernel /= np.sum(kernel)

    return kernel

def gaussianBlur(I):
    sigma = 2
    kernel_size = 5
    gaussianKernel = createFilter(sigma, kernel_size)
    rows, cols = I.shape
    blurred = I.copy()
    index = int(kernel_size / 2)
    for i in range(rows - kernel_size):
        for j in range(cols - kernel_size):
            window = I[i:i + kernel_size, j:j + kernel_size]
            temp = np.sum(np.multiply(window, gaussianKernel))
            if temp > 255:
                blurred[i:i + kernel_size, j:j + kernel_size][index][index] = 255
            elif temp < 0:
                blurred[i:i + kernel_size, j:j + kernel_size][index][index] = 0
            else:
                blurred[i:i + kernel_size, j:j + kernel_size][index][index] = temp

    return blurred

def gradient(I):
    rows, cols = I.shape
    gx = np.zeros(I.shape)
    gy = np.zeros(I.shape)
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and i - 1 >= 0:
                gx[i, j] = (int(I[i + 1, j]) - int(I[i - 1, j])) / 2
            if j + 1 < cols and j - 1 >= 0:
                gy[i, j] = (int(I[i, j + 1]) - int(I[i, j - 1])) / 2

    return gx, gy

def harris_corner(I, Ix, Iy, thresholdValue):
    rows, cols = I.shape
    I_WithCorner = I.copy()
    I_WithCorner = cv2.cvtColor(I_WithCorner, cv2.COLOR_GRAY2RGB)
    kernel_size = 3
    Ixx = Ix ** 2
    Iyy = Iy ** 2
    Ixy = Ix * Iy
    k = 0.04
    index = int(kernel_size / 2)
    for i in range(index, rows - index):
        for j in range(index, cols - index):
            Windowxx = Ixx[i - index:i + index + 1, j - index:j + index + 1]
            Windowxy = Ixy[i - index:i + index + 1, j - index:j + index + 1]
            Windowyy = Iyy[i - index:i + index + 1, j - index:j + index + 1]
            Sxx = np.sum(Windowxx)
            Sxy = np.sum(Windowxy)
            Syy = np.sum(Windowyy)
            determinant = (Sxx * Syy) - (Sxy ** 2)
            trace = Sxx + Sxy
            R = determinant - k * (trace ** 2)

            if R > thresholdValue:
                
                I_WithCorner = cv2.circle(I_WithCorner, (j, i), 3, (0, 0, 255), -1)
    return I_WithCorner

im = cv2.imread("test.png", 0)
blurred_img = gaussianBlur(im)
im_x, im_y = gradient(blurred_img)

threshold = 9000000

img_corner = harris_corner(blurred_img, im_x, im_y, threshold)



cv2.imshow("result.png", img_corner)
cv2.imwrite("part3.png",img_corner)
cv2.waitKey(0)
    