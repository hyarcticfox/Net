from socket import *
from threading import Thread

def sender(UDPSocket, addr):

    data = input('请输入：')
    UDPSocket.sendto(data.encode("GB2312"),addr)
    #sendto函数需要传入byte格式，即str的编码形式
def receiver(UDPSocket):

    recvData = UDPSocket.recvfrom(1024)  # recvData为一个元组，第一个元素为数据，第二个为地址的元组
    print("ip:%s,%s" % (recvData[1], recvData[0].decode('GB2312')))

if __name__ = '__main__':
    UDPSocket = socket(AF_INET, SOCK_DGRAM)
    UDPSocket.bind(('', 8989))  # 第一个参数不填说明绑定本机上的所有IP4 IP，和'0.0.0.0'同样效果
    addr = ('192.168.112.1', 8080)
    Thread1 = Thread(target = sender(UDPSocket, addr))
    Thread2 = Thread(target = receiver(UDPSocket))
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()
