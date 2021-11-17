import socket
from time import sleep

def addr_port():
    addr = str(input("Введите IP-адрес компьютера: "))
    port_name = str(input("Введите порт, по которому хотите подключиться: "))
    if(addr == ''):
        addr = "localhost"
    if(port_name == ''):
        port_name = 9090
    return addr, int(port_name)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.settimeout(0.1)
    address, port = addr_port()
    sock.connect((address, port))

    # msg = input()
    # sock.send(msg.encode())
    while True:
        try:
            msg = input("Введите сообщение: ")
            sock.send(msg.encode())
            try:
                data = sock.recv(1024)
                if(data.decode("UTF-8") == "exit"):
                    print("Вы отсоедины от сервера!")
                    break
            except:
                pass
            else:
                print("Message from: ", data.decode("UTF-8"))
            if(msg == "exit"):
                break
        except KeyboardInterrupt:
            print("Вы отсоедины от сервера!")
            msg = "exit"
            sock.send(msg.encode())
            break

    sock.close()

main()
