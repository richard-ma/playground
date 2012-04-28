#!/usr/bin/env clisp

(defun foo (&key x y) (cons x y))
(print (foo :x 5 :y 3))
(print (foo :y 3 :x 5))
(print (foo :y 3))
(print (foo))
