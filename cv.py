import cv2, sys, os
import numpy as np
from PIL import Image
from PyQt5 import QtGui, QtWidgets

def returnresult (a, b):

    return a-b


def pillingimage (image, w, h, x, y):

    resized_image = image[x:w+x,y:h+y]
    return resized_image

def VectorImage (image, vector):

    etalimage = cv2.imread(vector)

    return cv2.compareHist(image, etalimage, method="CV_COMP_INTERSECT")

def capdecode (captcha, method):

    im = Image.open(captcha)
    im = im.convert("P")
    his = im.histogram()

    return 0


def histimage (image):

    #This function will be wroten Abid Rahman K thanks for him

    img = image
    h = np.zeros((300, 256, 3))
    #Разделяем изображение на отдельные цветовые каналы
    b, g, r = cv2.split(img)
    bins = np.arange(256).reshape(256, 1)
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for item, col in zip([b, g, r], color):
        hist_item = cv2.calcHist([item], [0], None, [256], [0, 255])
        cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))
        pts = np.column_stack((bins, hist))
        cv2.polylines(h, [pts], False, col)


    h = np.flipud(h)
    return h

def histvideonum (image):

    global hist
    #This function will be wroten Abid Rahman K thanks for him

    img = image
    h = np.zeros((300, 256, 3))
    #Разделяем изображение на отдельные цветовые каналы
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([img], [ch], None, [256], [0, 255])
        cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))

    return hist

def histimagenum ():

    global hist
    #This function will be wroten Abid Rahman K thanks for him
    path = '/home/niki/Изображения/DSC_0142.JPG'
    img = cv2.imread(path)
    h = np.zeros((300, 256, 3))
    #Разделяем изображение на отдельные цветовые каналы
    #b, g, r = cv2.split(img)
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([img], [ch], None, [256], [0, 255])
        cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))

    return hist


def nothing(x):
    pass

global a
path = '/home/niki/Нагорье - Переславль Залесский.mp4'
cap = cv2.VideoCapture(path)
vec = "/home/Изображения/Обучалка/1510_1_1.jpg"
width = 50
height = 50
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
a = histimagenum()
while (True):

    ok, img = cap.read()

    for i in range(0,int(w)-1):
        for j in range (0, int(h)-1):

            img2 = img[int(i):int(j),int(i+w):int(j+h)]
            b = histvideonum(img2)




    cv2.imshow('in', img)
    cv2.imshow('out2', histimage(img))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

