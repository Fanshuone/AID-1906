from socket import *
from  time import sleep
sockfd = socket()
sockfd.bind(("192.168.0.105", 8880))
sockfd.listen(5)

connfd, addr = sockfd.accept()
file = open("R.jpg", "wb")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    sleep(0.01)
    file.write(data)

file.close()
sockfd.close()
connfd.close()