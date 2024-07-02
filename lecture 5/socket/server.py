"""import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1" , 5000))

s.listen(5)

while True:
    client , address = s.accept()
    rodata = client.recv(1024)
    print(f"{address} is sending to you this message {rodata.decode('UTF-8')}")
    print("============================")
    msg= str(input("please enter the message that you want to send : "))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    client.close()

    """

import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("Received data from client:", data)
        
    client_socket.close()



def server():
   
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.1.1", 5500))
    server.listen()
    print("enter your message: ")

    while True:
        client, addr = server.accept()
        print("New client connected:", addr)
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

server()