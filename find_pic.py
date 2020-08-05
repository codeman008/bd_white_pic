#!/usr/bin/env python
# -*- coding:utf-8 -*-

#从多文件夹里获取第一张张图
# import os
# import shutil
#
# path = "goods_data" #文件夹目录
# paths='pic_first/'
# files= os.listdir(path) #得到文件夹下的所有文件名称
#
# for i in files:
#     shutil.copy(path+"/"+i+"/"+"0.jpg",paths+i+'.jpg')


#从不同文件夹里获取白底图

from imutils import build_montages
from imutils import paths
import cv2
import imutils
import bg_detector as bg
import os
import numpy as np

path = "goods_data"
result=""
files=os.listdir(path)

for imagePath in paths.list_images(path):
    image = cv2.imdecode(np.fromfile(imagePath, dtype=np.uint8), -1)
    # print(imagePath.split('\\')[1])
    edge = bg.canny_edge(image)
    message = bg.detect_bg(image, 50)
    # if message=="Pure":
    #     print(imagePath.split('\\')[1])
    #     cv2.imencode(".jpg", image)[1].tofile("bd_white/" + imagePath.split('\\')[1] + '.jpg')
    if message=="bd_White":
        # cv2.imwrite("white_pic/"+imagePath.split('\\')[1]+'.jpg',image)
        cv2.imencode(".jpg", image)[1].tofile("bd_white/"+imagePath.split('\\')[1]+'.jpg')
        # print(imagePath.split('/')[0])

