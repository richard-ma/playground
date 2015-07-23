#!/usr/bin/env ruby
# -*- mode: ruby; coding: utf-8 -*-

# This is a tiny script to help you creating a CSV file from a face
# database with a similar hierarchie:
# 
#  philipp@mango:~/facerec/data/at$ tree
#  .
#  |-- README
#  |-- s1
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#
# See http://docs.opencv.org/trunk/modules/contrib/doc/facerec/facerec_tutorial.html
#
if ARGV.size != 1
  puts "usage: ruby #{__FILE__} <base_path>"
  exit
end

BASE_PATH = ARGV[0]
SEPARATOR = ';'

label = 0
Dir.glob("#{BASE_PATH}/*").each { |dir|
  if FileTest::directory? dir
    Dir.glob("#{dir}/*") { |filename|
      puts "#{filename}#{SEPARATOR}#{label}"
    }
    label += 1
  end
}

