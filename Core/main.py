#!/usr/bin/python3


#模块包含
from re import T
import socket
import sys
import threading
import time
import stopThreading
import network
import json



if __name__=="__main__":
    #树莓派专用
    #serverNO1 = TcpServer("192.168.31.119", 50000)
    #虚拟机专用
    serverNO1 = network.TcpServer("192.168.31.126", 50000)
    #阿里云服务器专用
    #serverNO1 = TcpServer("172.19.35.203", 50000)
    serverNO1.socket_start()

    data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    print ("Python 原始数据：", repr(data))
    print ("JSON 对象：", json_str)

    data2 = json.loads(json_str)
    print ("data2['name']: ", data2['name'])
    print ("data2['url']: ", data2['url'])

    while True:
        time.sleep(1)