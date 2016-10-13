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
# first line of data is variables name of values.
# return data array.
def load_data(data_file_name):
    global logger

    # check data file exsists
    if not check_file_exsists(data_file_name):
        logger.error("No such file: %s" % (data_file_name))

    # load it
    data = list()
    first_line_flg = True
    with open(data_file_name, 'rb') as datafile:
        reader = csv.reader(datafile)
        variables_name = list()
        reference_column = dict()

        for row in reader:
            if first_line_flg:
                # first line
                first_line_flg = False

                for element in row:
                    if ':' in element:
                        k, v = element.split(':')
                        logger.debug("k: %s, v: %s" % (k, v))
                        reference_column[k] = v
                    else:
                        variables_name.append(element)

                logger.debug("variables_name: %s" % (variables_name))
            else:
                # real data
                logger.debug("real data row: %s" % (row))

                parsed_row = dict(zip(variables_name, row))
                logger.debug("parsed_row: %s" % (parsed_row))

                for k, v in reference_column.iteritems():
                    parsed_row[k] = parsed_row[v]
                data.append(parsed_row)

    logger.debug("Data: %s" % (data))

    return data

# Replace & Write file
def write_result_file(generated_content, output_file_name, output_path = './output/'):
    output_file_name = "%s%s" % (output_path, output_file_name)
    output_file = open(output_file_name, 'w')
    output_file.write(generated_content)

def generate_for_one_line_data(template, one_line_data):
    global logger

    for k, v in one_line_data.iteritems():
        old = "{$%s}" % (k)
        new = v
        if k == 'output_file':
            # skipped output_file column
            logger.debug("Skipped output_file column")
            continue
        else:
            template = template.replace(old, new)
            logger.debug("Replacing %s -> %s" % (old, new))
    return template

def generate(template, data):
    global logger

    for one_line_data in data:
        # get result
        result = generate_for_one_line_data(template, one_line_data)
        logger.debug("Result: %s" % (result))

        # get output file name
        output_file_name = one_line_data['output_file'] # get output file name form data 'output_file' column
        logger.debug("Output file name: %s" % (output_file_name))

        # write file
        write_result_file(result, output_file_name)

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

    # generate result and write to file
    generate(template, data)

# Global Variables
logger = enable_logger(logging.DEBUG)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        main(sys.argv)
