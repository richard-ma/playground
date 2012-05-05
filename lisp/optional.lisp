#!/usr/bin/env clisp

(defun bar (x &optional y) (if y x 0))
(defun baaz (&optional (x 3) (z 10)) (+ x z))

(print (bar 5))
(print (bar 5 t))
(print (baaz 5))
(print (baaz 5 6))
(print (baaz))
