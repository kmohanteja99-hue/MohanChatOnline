import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

clients = []

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(message):
    for client in clients:
        client.send(message)

print("Server running...")

while True:
    client, address = server.accept()
    print("Connected:", address)
    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
