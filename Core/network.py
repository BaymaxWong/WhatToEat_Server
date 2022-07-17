#网络模块，用于TCP、UDP的服务、客户端建立连接与通信

from re import T
import socket
import sys
import threading
import time
import stopThreading
import json
import http

#服务器http端口
def socket_server_callback_get(socket):
    print("线程开启")

    revdata = socket.recv(1024)
    if revdata:
        #socket.send(revdata)
        senData = http.get_response(revdata)
        socket.send(senData)

    socket.close()
    print("线程关闭")


#服务器端口
def socket_server_callback_task(socket):
    print("线程开启")
    while True:
        try:
            revdata = socket.recv(1024)
            if revdata:
                socket.send(revdata)
            else:
                break
        except Exception:
            socket.close()
            break
    print("线程关闭")

class TcpServer():
    def __init__(self, host, port):
        #储存host与port传参
        self.host = host
        self.port = port
        self.tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #定义tcp客户端socket与线程句柄
        self.tcpc = None
        self.th = None

    def socket_start(self):
        try:
            #绑定host与port
            self.tcps.bind((self.host, self.port))
            #设置最大连接数
            self.tcps.listen(5)
        except Exception as ret:
            print('Error:', ret)
        else:
            #开启服务器监听线程
            print("开启TcpServer端口监控线程")
            self.th = threading.Thread(target=self.socket_work)
            self.th.setDaemon(True)
            self.th.start()

    def socket_work(self):
        print("TcpServer端口监控线程开启成功")
        self.tcpc_th = None
        while True:
            print("服务器监听IP端口为" + self.host + ":" ,self.port)
            self.tcpc, addr = self.tcps.accept()
            print("服务器"+ self.host + ":" + str(self.port) +"已被连接, 来源地址:" + str(addr))
            threading.Thread(target=socket_server_callback_get, args = (self.tcpc,)).start()
    

def socket_client_callback_task(socket):
    print("线程开启")
    while True:
        try:
            revdata = socket.recv(1024)
            if revdata:
                socket.send(revdata)
            else:
                break
        except Exception:
            socket.close()
            break
    print("线程关闭")

class TcpClient():
    def __init__(self, host, port):
        #储存host与port传参
        self.host = host
        self.port = port
        self.tcpc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #定义tcp客户端socket与线程句柄
        self.tcpc = None
        self.th = None

    def socket_start(self):
        try:
            #绑定host与port
            self.tcps.bind((self.host, self.port))
            #设置最大连接数
            self.tcps.listen(5)
        except Exception as ret:
            print('Error:', ret)
            self.socket_close()
        else:
            #开启服务器监听线程
            print("开启TcpServer端口监控线程")
            self.th = threading.Thread(target=self.socket_work)
            self.th.setDaemon(True)
            self.th.start()

    def socket_work(self):
        print("TcpServer端口监控线程开启成功")
        self.tcpc_th = None
        while True:
            print("服务器监听IP端口为" + self.host + ":" ,self.port)
            self.tcpc, addr = self.tcps.accept()
            print("服务器"+ self.host + ":" + str(self.port) +"已被连接, 来源地址:" + str(addr))
            threading.Thread(target=socket_server_callback_task, args = (self.tcpc,)).start()



#if __name__=="__main__":
    #树莓派专用
    #serverNO1 = TcpServer("192.168.31.119", 50000)
    #虚拟机专用
    #serverNO1 = TcpServer("192.168.31.126", 50000)
    #阿里云服务器专用
    #serverNO1 = TcpServer("172.19.35.203", 50000)
    #serverNO1.socket_start()

    #a = 0
    #while True:
     #   a = a + 1
    #    print("a:",a)
     #   time.sleep(1)


