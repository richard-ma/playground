#!/usr/bin/env clisp

(defun foo (x &rest y) y)

(print (foo 3))
(print (foo 4 5 6))
