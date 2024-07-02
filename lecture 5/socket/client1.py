"""import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",5000))
print("============================")

msg = str(input("please enter the message that you want to send : "))
msg_encoded = msg.encode('UTF-8')
client.send(msg_encoded)
print("============================")
rodata = client.recv(1024)
print(f"127.0.0.1 is sending to you with message {rodata.decode('UTF-8')}")
client.close()
"""

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