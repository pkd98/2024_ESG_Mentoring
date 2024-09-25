import socket
import threading

# 서버 IP와 포트 설정
HOST = '127.0.0.1'
PORT = 12345

# 서버 소켓 생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # 연결된 클라이언트 목록: {client: nickname}

# 클라이언트로부터 메시지를 수신하고 브로드캐스트하는 함수
def handle_client(client, nickname):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise ConnectionResetError
            print(f"Received: {message.decode('utf-8')}")  # 서버 로그 출력
            broadcast(message, client)
        except:
            # 클라이언트가 끊어진 경우
            clients.pop(client, None)
            broadcast(f"{nickname}님이 퇴장하셨습니다.".encode('utf-8'), None)
            client.close()
            break

# 메시지를 모든 클라이언트에게 전송하는 함수
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                clients.pop(client, None)

# 새로운 클라이언트를 수락하는 함수
def receive():
    while True:
        client, address = server.accept()
        client.send(b"NICK")  # 닉네임 요청
        nickname = client.recv(1024).decode('utf-8')
        clients[client] = nickname
        print(f"Connected with {address}, Nickname: {nickname}")
        
        # 입장 알림 메시지를 모든 클라이언트에게 전송
        broadcast(f"{nickname}님이 들어오셨습니다.".encode('utf-8'), None)

        # 클라이언트 핸들링 스레드 시작
        thread = threading.Thread(target=handle_client, args=(client, nickname))
        thread.start()

print("Server is running...")
receive()
