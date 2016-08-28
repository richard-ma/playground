#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import csv
import shutil

input_filename = 'test.csv'
output_notfound_filename = 'nofound.csv'
output_found_filename = 'newimages.csv'
input_image_path = './images'
output_image_path = './newimages'

def load_data(input_filename):
    # check input data file
    if not os.path.exists(input_filename):
        print '请先创建test.csv文件'
        quit()

    input_file = open(input_filename, 'rb') # open file
    data = list(csv.reader(input_file)) # convert to list
    input_file.close()
    return data[1:] # remove first element

def decode_filename(filename):
    return filename.decode('gbk')

def check_image(image_filename):
    image_filename = image_filename + '.jpg'
    if os.path.exists(os.path.join(input_image_path, image_filename)):
        return True
    else:
        return False

def write_not_found(output_filename, data):
    data.insert(0, ['code', 'image']);
    with open(output_filename, 'wb') as f:
        w = csv.writer(f)
        w.writerows(data)

def write_find(output_filename, output_image_path, data):
    # check path
    if not os.path.exists(output_image_path):
        print '请先创建newimages目录'
        quit()

    # move and rename image files
    for r in data:
        old_filename = os.path.join(input_image_path, decode_filename(r[1]) + '.jpg')
        new_filename = os.path.join(output_image_path, r[2])
        shutil.move(old_filename, new_filename)

    # write data
    data.insert(0, ['code', 'image', 'newimages']);
    with open(output_filename, 'wb') as f:
        w = csv.writer(f)
        w.writerows(data)

if __name__ == '__main__':
    data = load_data(input_filename)

    find = list()
    notfound = list()

    for r in data:
        filename = decode_filename(r[1])
        if check_image(filename):
            # find image
            r.append(r[0] + '.jpg') # add new image filename
            find.append(r)
        else:
            # not find image
            notfound.append(r)

    write_find(output_found_filename, output_image_path, find)
    write_not_found(output_notfound_filename, notfound)
