import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',80))
if result == 0:
   print("Port is open")
else:
   print("Port is not open")
sock.close()