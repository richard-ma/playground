#!/usr/bin/env clisp

(defun fact (x)
  (if (> x 0)
    (* x (fact (- x 1)))
    1))

(print (fact 5))
(print (fact 10))
