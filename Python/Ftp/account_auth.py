#!/usr/bin/python
#-*-coding:utf-8 -*-

import os
import sys
import time
import signal
import datetime

from ftplib import FTP


"""
===ftp_account.txt content===
user1   passwd1
user2   passwd2
user3   passwd3
"""


#======================================
def sigHandle(sig, frame):
    print('\nPython script terminated')
    os._exit(0)

signal.signal(signal.SIGINT, sigHandle)
#======================================


if os.path.exists('./ftp_account.txt'):
    fd = open('./ftp_account.txt', 'r')
else:
    print "no such file"
    os._exit(-1)

ftp = FTP()
i = 0
j = 0
MAX = 0
fail_dict = {}
while 1:
    line = fd.readline()
    if not line:
        break

    line = line.strip('\n').split()
    if len(line) != 2:
        print "wrong file format, break..."
        #!/usr/bin/python
#-*-coding:utf-8 -*-

import os
import sys
import time
import signal
import datetime

from ftplib import FTP


"""
===ftp_account.txt content===
user1   passwd1
user2   passwd2
user3   passwd3
"""


#======================================
def sigHandle(sig, frame):
    print('\nPython script terminated')
    os._exit(0)

signal.signal(signal.SIGINT, sigHandle)
#======================================


if os.path.exists('./ftp_account.txt'):
    fd = open('./ftp_account.txt', 'r')
else:
    print "no such file"
    os._exit(-1)

ftp = FTP()
i = 0
j = 0
MAX = 0
fail_dict = {}
while 1:
    line = fd.readline()
    if not line:
        break

    line = line.strip('\n').split()
    if len(line) != 2:
        print "wrong file format, break..."
        continue

    try:
        print "正在测试 %s" % line[0]
        ftp.connect(host="192.168.1.49", timeout=30)
        ftp.login(line[0], line[1])
        ftp.close()
        i += 1
    except Exception as e:
        if len(line[0]) > MAX:
            MAX = len(line[0])

        fail_dict[line[0]] = str(e)
        j += 1

print "成功%d个," % i + "失败%d个" % j
for each in fail_dict:
    print("失败账号: {:<%d}," % MAX).format(each) + \
        (" 失败原因: {:<%d}" % MAX).format(fail_dict[each])


    try:
        print "正在测试 %s" % line[0]
        ftp.connect(host="miguvideolog.cmvideo.cn", timeout=30)
        ftp.login(line[0], line[1])
        ftp.close()
        i += 1
    except Exception as e:
        if len(line[0]) > MAX:
            MAX = len(line[0])

        fail_dict[line[0]] = str(e)
        j += 1

print "成功%d个," % i + "失败%d个" % j
for each in fail_dict:
    print("失败账号: {:<%d}," % MAX).format(each) + \
        (" 失败原因: {:<%d}" % MAX).format(fail_dict[each])
