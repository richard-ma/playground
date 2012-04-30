#!/usr/bin/env python
#--* encoding: utf-8 *--

import wx
import cv

class VideoFrame(wx.Frame):
    def __init__(self, cam_id=-1):
        wx.Frame.__init__(self, None, -1, 'camera')
        self.cap = cv.CreateCameraCapture(cam_id)
        #print self.cap
        w = cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_WIDTH)
        h = cv.GetCaptureProperty(self.cap, cv.CV_CAP_PROP_FRAME_HEIGHT)
        self.SetClientSize((w, h))
        self.SetTitle('camera.%s %sx%s' % (cam_id, int(w), int(h)))

        self.Bind(wx.EVT_IDLE, self.onIdle)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onIdle(self, event):
        frame = cv.QueryFrame(self.cap)
        #self.SetSize((frame.width, frame.height))
        image = self.make_image(frame)
        self.displayImage(image)
        event.RequestMore()

    def make_image(self, frame):
        image_size = cv.GetSize(frame)

        grayscale = cv.CreateImage(image_size, 8, 1)# 建立一个空的灰度图
        cv.CvtColor(frame, grayscale, cv.CV_BGR2GRAY)#转换

        storage = cv.CreateMemStorage(0)#新建一块存储区，以备后用

        cv.EqualizeHist(grayscale, grayscale)# 灰度图直方图均衡化

        # detect objects
        cascade = cv.Load('haarcascade_frontalface_alt.xml')
        faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, 0,
                (50, 50))#设置最小的人脸为50*50像素

        if faces:
            print 'face detected here', cv.GetSize(grayscale)
            for i in faces:
                print i[0][0]
                cv.Rectangle(frame, (i[0][0], i[0][1]),
                        (i[0][0] + i[0][2], i[0][1] + i[0][3]),
                        cv.CV_RGB(0, 255, 0), 1, 8, 0)#画一个绿色的矩形框
        cv.CvtColor(frame, frame, cv.CV_BGR2RGB) # Color correction, if you don't do this your image will be greenish

        bitmap = wx.BitmapFromBuffer(frame.width, frame.height, frame.tostring())
        return bitmap

    def displayImage(self, bitmap, offset=(0,0)):
        dc = wx.ClientDC(self)
        dc.DrawBitmap(bitmap, offset[0], offset[1], False)

    def onClose(self, event):
        import sys
        sys.exit(0)

if __name__=="__main__":
    app = wx.App()
    frame = VideoFrame(0)
    frame.Show(True)
    app.MainLoop()
