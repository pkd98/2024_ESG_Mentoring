import socket
import threading

# 서버의 IP 주소와 포트 설정
HOST = '127.0.0.1'  # localhost
PORT = 5000

# 클라이언트와의 연결 처리
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Client: {message}")
            else:
                break
        except:
            break

    client_socket.close()

# 서버 소켓 설정
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server is listening on {HOST}:{PORT}")

# 클라이언트 연결 수락
client_socket, addr = server.accept()
print(f"Accepted connection from {addr}")

# 스레드를 이용해 클라이언트와 통신
thread = threading.Thread(target=handle_client, args=(client_socket,))
thread.start()

# 서버에서 메시지 전송
while True:
    message = input("Server: ")
    client_socket.send(message.encode())
