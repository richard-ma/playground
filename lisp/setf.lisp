#!/usr/bin/env clisp

(setq a (make-array 3))
(print (aref a 1))
(setf (aref a 1) 3)
(print a)
