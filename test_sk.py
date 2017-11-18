import socket

HOST = "localhost"
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind failed. Error Code : ' .format(err))
s.listen(10)
print("Socket Listening")
conn, addr = s.accept()
while(True):
    #Data send to client
    conn.send(bytes("Message"+" Hello\r\n",'UTF-8'))
    print("Message sent")
    #Data receive from server
    #data = conn.recv(1024)
    #print(data.decode(encoding='UTF-8'))