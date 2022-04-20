from socket import *

# 创建tcp套接字"192.168.0.105", 8888
sockfd = socket()
# 连接服务器
sockfd.connect(("192.168.0.105", 8889))
# 发送消息
while True:
    data = input("Msg<<")
    if not data:
        break
    sockfd.send(data.encode()) # 转换为字节串在发送

    data = sockfd.recv(1024)
    print("Server", data.decode()) # 打印接收内容

sockfd.close()

