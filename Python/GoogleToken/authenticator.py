#!/usr/bin/python
#-*-coding:utf-8 -*-

import hmac
import base64
import struct
import hashlib
import time

# token是8的倍数，不足则以=补足
gtoken = "J4RKWWTNYCT6QB4NB4HNDAQ5BU======"
key = base64.b32decode(gtoken, True)
msg = struct.pack(">Q", int(time.time()) // 30)
h = hmac.new(key, msg, hashlib.sha1).digest()
o = ord(h[19]) & 15
h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
print "username"
print "password" + "%06d" % h
