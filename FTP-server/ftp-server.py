import socket
import os
import ftplib
'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
'''
admin = 0
user = 0

dirname = os.path.join(os.getcwd(), 'docs')

def process(req):
    global user
    if req == 'pwd':
        return dirname
    elif req == 'whoami':
        return os.getlogin()
    elif 'register' in req:
        user = str(req.split()[1]) + "^" + str(req.split()[2])
        file = open ('users.txt','+a')
        file.write(user + "___")
        return 'reg'
    elif 'login' in req:
        user = str(req.split()[1]) + "^" + str(req.split()[2])
        file = open ('users.txt','+a')
        l = [line.split("___") for line in file]
        print(l)
        return 'reg'
    elif req == 'exit':
        return str(False)
    elif req == 'dir':
        return str(os.listdir(path="."))
    elif 'mkdir' in req:
        os.mkdir(req.split()[1])
    elif 'rmdir' in req:
        os.rmdir(req.split()[1])
    elif 'remove' in req:
        os.remove(req.split()[1])
    elif 'rename' in req:
        os.rename(req.split()[1],req.split()[2])
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    return 'bad request'


PORT = 6666

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)

    if response == "reg":
        response = "USER created" + str(user)
        conn.send(response.encode())


    conn.send(response.encode())

    if response == "False":
        break


conn.close()

# req = req.split()[1]
#         file = open("/var/www/a1.com/access.txt",'r')
#         l = [line.split('\n') for line in file]
#         table = []
#         for i in range (0,len(l)):
#             table.append(l[i])
#         file.close()