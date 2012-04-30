#!/usr/bin/env python
#--* encoding: utf-8 *--

import cv

if __name__ == "__main__":
    cap = cv.CreateCameraCapture(0)
    frame = cv.QueryFrame(cap)
    cv.NamedWindow('camera', cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage('camera', frame)
    cv.WaitKey(0)
