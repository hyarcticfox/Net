from socket import *

UDPSocket = socket(AF_INET, SOCK_DGRAM)
UDPSocket.bind(('',8989)) #第一个参数不填说明绑定本机上的所有IP4 IP，和'0.0.0.0'同样效果
recvData = UDPSocket.recvfrom(1024)  #recvData为一个元组，第一个元素为数据，第二个为地址的元组
print("ip:%s,%s"%(recvData[1],recvData[0].decode('GB2312')))v

