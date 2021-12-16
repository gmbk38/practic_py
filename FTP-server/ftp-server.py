import socket
import os
import ftplib
'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
'''
admin = 0
admin_login = "cyberpunk"
admin_pwd = "1234"
login = 0
user = 0
dirname = None

def process(req):
    global login
    global user
    global dirname
    if req == 'pwd' and login != 0:
        return dirname
    elif req == 'whoami':
        return os.getlogin()
    elif 'register' in req:
        user = str(req.split()[1]) + "^" + str(req.split()[2])
        file = open ('users.txt','+a')
        file.write(user + "___")
        return 'reg'
    elif 'login' in req:
        if str(req.split()[1]) == admin_login and str(req.split()[2]) == admin_pwd:
            login = admin_login
            dirname = os.path.join(os.getcwd())
            return 'admin'
        user = str(req.split()[1]) + "^" + str(req.split()[2])
        req = req.split()[1]
        file = open("users.txt",'r')
        database = [line.split('___') for line in file]
        database = database[0]
        file.close()
        main_data = []
        for u in database:
            if u == user:
                try:
                    os.mkdir(req)
                except FileExistsError:
                    pass
                return 'user_ok'
        return 'user_false'
    elif req == 'exit':
        return str(False)
    elif req == 'dir' and login != 0 and login != admin_login:
        return str(os.listdir(path="."))
    elif 'mkdir' in req and login != 0 and login != admin_login:
        os.mkdir(login + '/' + str(req.split()[1]))
        return "папка создана"
    elif 'rmdir' in req and login != 0 and login != admin_login:
        os.rmdir(login + '/' + str(req.split()[1]))
        return "папка удалена"
    elif 'remove' in req and login != 0 and login != admin_login:
        os.remove(login + '/' + str(req.split()[1]))
        return "файл удален"
    elif 'rename' in req and login != 0 and login != admin_login:
        os.rename(login + '/' + str(req.split()[1]), login + '/' + str(req.split()[2]))
        return "файл переименован"
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    #Команды для админа
    elif req == 'dir' and login == admin_login:
        return str(os.listdir(path="."))
    elif 'mkdir' in req and login == admin_login:
        os.mkdir(str(req.split()[1]))
        return "папка создана"
    elif 'rmdir' in req and login == admin_login:
        os.rmdir(str(req.split()[1]))
        return "папка удалена"
    elif 'remove' in req and login == admin_login:
        os.remove(str(req.split()[1]))
        return "файл удален"
    elif 'rename' in req and login == admin_login:
        os.rename(str(req.split()[1]),str(req.split()[2]))
        return "файл переименован"
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif login == '0':
        return "Вы не выполнили вход"


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
        response = "USER created"
        conn.send(response.encode())

    if response == "user_ok":
        login = request.split()[1]
        dirname = os.path.join(os.getcwd(), str(login))
        # print(login)


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