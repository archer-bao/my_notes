#!/usr/bin/python3

import requests
import sys
import re
import os

headers = {
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CA;q=0.8,en;q=0.7'
}


def get_songs(url):
    res = requests.get(url, headers=headers)
    name = re.findall(r'"title": "[\w\W\u4e00-\u9fff]+?"', res.text)
    listpath = ''
    for n in name:
        print(n[10:-1])
        listpath = n[10:-1]
        folder = os.path.exists(listpath)
        if not folder:
            print("make folder")
            os.makedirs(listpath)
    index = 0
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        index += 1
        print(index, ": ",i[0],"  ", i[1])
        try:
            with open(listpath+'/' + i[1] + '.mp3', 'wb') as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            print("exception 1")
            pass
        except OSError:
            print("exception 2")
            pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_songs(sys.argv[1])
    else:
        playlist = ["https://music.163.com/playlist?id=533197318",
                    "https://music.163.com/playlist?id=97344707",
                    "https://music.163.com/playlist?id=117586346",
                    "https://music.163.com/playlist?id=427850291",
                    "https://music.163.com/playlist?id=9274810",
                    "https://music.163.com/playlist?id=6220214",
                    "https://music.163.com/playlist?id=23597339",
                    "https://music.163.com/playlist?id=8608439",
                    "https://music.163.com/playlist?id=8155635"]
                    
        for each in playlist:
            get_songs(each)
