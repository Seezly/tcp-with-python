import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 666

s.bind((host, port))

s.listen(3)

while True:

    conn, addr = s.accept()

    print(addr, "Now Connected")

    conn.send("Thank you for connecting")

    conn.close()