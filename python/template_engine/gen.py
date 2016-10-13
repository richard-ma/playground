#!/usr/bin/env python

import sys
import logging
import logging.handlers
import csv
import os

# Load Template
# template file is end with .tpl in template directory.
# return template string.
def load_template(template_file_name):
    global logger

    # check template file exsists
    if not check_file_exsists(template_file_name):
        logger.error("No such file: %s" % (template_file_name))

    # load it
    template_file = open(template_file_name, 'r')
    template = template_file.read()

    logger.debug("Template: %s" % (template))

    return template

# Load Data
# data file is end with .csv in data directory.
# data file write with csv format, and load it to array.
# return data array.
def load_data(data_file_name):
    global logger

    # check data file exsists
    if not check_file_exsists(data_file_name):
        logger.error("No such file: %s" % (data_file_name))

    # load it
    data = []
    with open(data_file_name, 'rb') as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            data.append(row)

    logger.debug("Data: %s" % (data))

    return data

# Replace & Write file
def write_output(generate_content, output_file_name, output_path = './output/'):
    pass

def replace(template, data):
    pass

def usage():
    print "Usage: \n"
    print "./gen.py (name) \n"

def check_file_exsists(file_name):
    return os.path.isfile(file_name)

def enable_logger(level = logging.ERROR):
    # log file name
    log_file_name = './log.log'

    # Set logging handler
    handler = logging.handlers.RotatingFileHandler(log_file_name,
            maxBytes = 1024 * 1024,
            backupCount = 5)

    # Setting logging format
    fmt = "%(asctime)s [%(levelname)s] %(filename)s[%(lineno)s]:%(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger

def main(argv):
    global logger

    name = argv[1]
    logger.debug("name: %s" % (name))

    # load template
    template_file_name = "./template/%s.tpl" % (name)
    logger.debug("Template file name: %s" % (template_file_name))
    template = load_template(template_file_name)

    # load data
    data_file_name = "./data/%s.csv" % (name)
    logger.debug("Data file name: %s" % (data_file_name))
    data = load_data(data_file_name)

# Global Variables
logger = enable_logger(logging.DEBUG)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        main(sys.argv)
