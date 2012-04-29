#!/usr/bin/env python

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
