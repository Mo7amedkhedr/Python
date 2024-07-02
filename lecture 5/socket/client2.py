import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print("your ip is: "+ip)
client.connect((ip,5500))
print("=========================================")

while True:
    msg=str(input("enter massage : "))
    msg_encode=msg.encode('UTF-8')
    client.send(msg_encode)
    print("======================================")
    msg_len=client.recv(1024)
    print(f"{ip} ifsending to this message {msg_len.decode('UTF-8')}")
    client.close()