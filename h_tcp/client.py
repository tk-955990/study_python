import socket
host = "127.0.0.1"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("This is a test". encode("UTF-8"))
