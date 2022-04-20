import socket
# 创建tcp套接字
sockfd = socket.socket()
# 绑定地址
sockfd.bind(("192.168.0.105", 8889))
# 设置监听
sockfd.listen(5)
# 阻塞等待处理连接
while True:
    print("waiting for connect")

    connfd, addr = sockfd.accept()

    print("connect from:", addr) # 打印链接的客户端地址
    while True:
        # 收发消息
        data = connfd.recv(1024)
        if not data:
            break
        print("收到：", data.decode())

        n = connfd.send("thanks".encode()) # 发送字节串

        print("发送%d字节" %n)

    connfd.close()

sockfd.close()



