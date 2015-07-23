#!/usr/bin/env ruby
# inpaint.rb
require "rubygems"
require "opencv"
include OpenCV

puts <<EOS
Inpainting sample

Usage:
  'dilate' bar - Adjust mask to inpaint (Non-black areas indicate the area that needs to be inpainted).
  'radius' bar - Adjust radius of a circular neighborhood of each point inpainted.
  'n' key - Inpaint using Navier-Stokes based method
  't' key - Inpaint using Alexandru Telea's method
  'c' key - Clear the inpaint window
  'ESC' key - exit"
EOS

owindow = GUI::Window.new('original')
mwindow = GUI::Window.new('mask')
iwindow = GUI::Window.new('inpaint')

image = IplImage::load('images/inpaint.png')
noimage = image.zero
b, g, r = image.split
original_mask = r.threshold(0x00, 0xFF, CV_THRESH_BINARY_INV) & b.threshold(0x00, 0xFF, CV_THRESH_BINARY_INV)
mask = original_mask.copy

num_dilate = 3
mwindow.set_trackbar("dilate", 10, num_dilate) { |v|
  num_dilate = v
  mask = original_mask.dilate(nil, num_dilate)
  mwindow.show mask  
}

radius = 5
mwindow.set_trackbar("radius", 10, radius) { |v|
  radius = v
}

owindow.show image
mwindow.show mask
iwindow.show noimage

while key = GUI::wait_key
  case key.chr
  when "\e" # esc
    exit
  when "n"
    iwindow.show image.inpaint(:ns, mask, radius)
  when "t"
    iwindow.show image.inpaint(:telea, mask, radius)
  when "c"
    iwindow.show noimage
  end
end

