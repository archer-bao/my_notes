#!/usr/bin/python
#-*-coding:utf-8 -*-

import os
import sys
import time
import datetime

from ftplib import FTP


"""
===ftp_account.txt content===
user1   passwd1
user2   passwd2
user3   passwd3
"""

if os.path.exists('./ftp_account.txt'):
    fd = open('./ftp_account.txt', 'r')
else:
    print "no such file"
    os._exit(-1)

ftp = FTP()
i = 0
j = 0
fail_dict = {}
while 1:
    line = fd.readline()
    if not line:
        break

    line = line.strip('\n').split()
    if len(line) != 2:
        print "wrong file format"
        os._exit(-2)

    try:
        ftp.connect(host="miguvideolog.cmvideo.cn", timeout=10)
        ftp.login(line[0], line[1])
        ftp.close()
        i += 1
    except Exception as e:
        fail_dict[line[0]] = str(e)
        j += 1

print "成功%d个," % i + "失败%d个" % j
for each in fail_dict:
    print "失败账号: %s,"%each+ " 失败原因: %s" % fail_dict[each]
