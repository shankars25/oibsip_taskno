import socket
import threading

HOST = '127.0.0.1'  
PORT = 12345        

def handle_client(client_socket, other_client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                other_client_socket.send(message.encode('utf-8'))
            else:
                break
        except:
            break
    client_socket.close()
    other_client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Server is listening for connections...")

    client1, addr1 = server.accept()
    print(f"Connected to {addr1}")
    client1.send("You are connected. Waiting for the other user...".encode('utf-8'))

    client2, addr2 = server.accept()
    print(f"Connected to {addr2}")
    client2.send("You are connected. Start chatting!".encode('utf-8'))
    client1.send("Both users connected. Start chatting!".encode('utf-8'))

    threading.Thread(target=handle_client, args=(client1, client2)).start()
    threading.Thread(target=handle_client, args=(client2, client1)).start()

if __name__ == "__main__":
    main()
