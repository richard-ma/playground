#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import socket
import time

current_ip = None

def ddns(ip):
    data = {
        'login_token': getToken(),
        'format': 'json',
        'domain_id': '10785701',
        'record_id': '223819089',
        'sub_domain': 'pi',
        'record_type': 'A',
        'record_line': '默认',
        'value': ip,
    }
    r = requests.post('https://dnsapi.cn/Record.Modify', data)
    return r.json()

def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip

def getToken():
    return '17517,bf8d60368dd3ede6777966466c5c3171'


if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            #print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
        time.sleep(30)
