#!/usr/bin/env python
#--* encoding: utf-8 *--

import cv
if __name__ == "__main__":
    image = cv.LoadImage('face2.jpg')
    image_size = cv.GetSize(image)

    grayscale = cv.CreateImage(image_size, 8, 1)# 建立一个空的灰度图
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)#转换

    storage = cv.CreateMemStorage(0)#新建一块存储区，以备后用

    cv.EqualizeHist(grayscale, grayscale)# 灰度图直方图均衡化

    # detect objects
    cascade = cv.Load('haarcascade_frontalface_alt.xml')
    faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, 0,
            (20, 20))#设置最小的人脸为20*20像素
    print faces

    if faces:
        print 'face detected here', cv.GetSize(grayscale)
        for i in faces:
            print i[0][0]
            cv.Rectangle(image, (i[0][0], i[0][1]),
                    (i[0][0] + i[0][2], i[0][1] + i[0][3]),
                    cv.CV_RGB(0, 255, 0), 1, 8, 0)#画一个绿色的矩形框

    cv.NamedWindow('camera', cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage('camera', image)
    cv.WaitKey(0)
