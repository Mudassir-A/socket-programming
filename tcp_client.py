import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    message = input("Enter String: ")
    server.send(bytes(message, "utf-8"))
    ack = server.recv(1024)
    ack = ack.decode("utf-8")
    print("Server: ", ack)
