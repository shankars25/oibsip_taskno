import socket
import threading

HOST = '127.0.0.1'  
PORT = 12345        

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print("\n" + message)
            else:
                break
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to the server. Start typing your messages.")

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        if message.lower() == 'exit':
            client.send('User has left the chat.'.encode('utf-8'))
            break
        client.send(message.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()

