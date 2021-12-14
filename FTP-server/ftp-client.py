import socket

HOST = 'localhost'
PORT = 6666

while True:
    request = input('>')
    
    sock = socket.socket()
    sock.connect((HOST, PORT))
    
    sock.send(request.encode())
    
    response = sock.recv(1024).decode()
    print(response)
    
    if response == "False":
        print("Соединение завершено")
        break

    if response == "sc":
       f = open("copy" + str(request.split()[1]),"w")
       while True:
           buf = sock.recv(1024).decode()
           print = buf + "1"
           f.write (buf + '\n')
           if buf == "":
              break
    

    sock.close()