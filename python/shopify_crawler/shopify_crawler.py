#!/usr/bin/env python

import sys
import os
import requests
import re
from collections import deque

# data format
# complete domain -> list
# seed domain -> list
# new domain -> Seed domain -> Completed domain

def load_complete_domains(complete_domains_file_name):
    return load_domains(complete_domains_file_name)

def load_seed_domains(seed_domains_file_name):
    return load_domains(seed_domains_file_name)

def load_domains(file_name):
    if not os.path.isfile(file_name):
        print "Cann't find file: %s" % (file_name)
        sys.exit(1)

    return deque([line.strip() for line in open(file_name, 'r')])

def save_complete_domains(complete_domains_file_name, complete_domains):
    save_domains(complete_domains_file_name, complete_domains, 'a')

def save_seed_domains(seed_domains_file_name, seed_domains):
    save_domains(seed_domains_file_name, seed_domains, 'w')

def save_domains(file_name, domains, save_type):
    f = open(file_name, save_type)
    f.writelines(["%s\n" % (element) for element in domains])

def reversed_query(domain):
    url = "http://www.114best.com/ip/114.aspx?w=%s" % (domain)
    #cookies = {
    #        '__jsluid': '118a44904176bcf9c4461bcd13d4bb79',
    #        'cck_lasttime': '1476405982747',
    #        'cck_count': '0'}
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
            }
    r = requests.get(url, headers=headers)
    domains = re.findall(r'(.*)</span>', r.text)
    domains = [element.strip().encode('utf-8') for element in domains[1:]]
    return domains

def check_new_domain(domain, complete_domains, seed_domains):
    if domain in seed_domains or domain in complete_domains:
        return False
    else:
        return True

def main(argv):
    # load complete domains
    complete_domains_file_name = 'complete.domains'
    complete_domains = load_complete_domains(complete_domains_file_name)
    print '# Load Complete Domain(s): %d' % (len(complete_domains))

    # load seed domains
    seed_domains_file_name = 'seed.domains'
    seed_domains = load_seed_domains(seed_domains_file_name)
    print '# Load Seed Domain(s): %d' % (len(seed_domains))
    print seed_domains

    while len(seed_domains) > 0:
        domain = seed_domains[0] # get current domain (seed_domains first one)
        print '#[C: %d/S: %d] Currect Domain: %s' % (len(complete_domains), len(seed_domains), domain)

        new_domains = reversed_query(domain)
        for d in new_domains:
            if check_new_domain(d, complete_domains, seed_domains):
                seed_domains.append(d) # add new domain to seed_domains

        complete_domains.append(domain) # add current domain to complete_domains
        # save current domains to file
        save_complete_domains(complete_domains_file_name, domain)

        # remove current domains
        seed_domains.popleft()
        # save seed_domains to file
        save_seed_domains(seed_domains_file_name, seed_domains)

if __name__ == '__main__':
    main(sys.argv)
