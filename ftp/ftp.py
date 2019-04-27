#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
from datetime import datetime


# 优雅的获得 ip 地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        try:
            if os.name == 'nt':
                # Windows 下获取 ip 地址的方法
                ip = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
            else:
                # Linux 下获取 ip 地址的方法
                ip = os.popen("ifconfig | grep inet").readlines()[0].strip().split(' ')[1]
        except:
            ip = None
    finally:
        s.close()
    return ip


def show_dir_file():
    files = os.listdir('./static/share')
    content = {"content": files}
    return content


def upload_to_dir(file_name, file):
    with open('./static/share/{0}'.format(file_name), 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)

    return True


# 今天是周五吗
def today_is_friday():
    friday = datetime.now().weekday()

    if friday == 4:
        return True
    else:
        return False
