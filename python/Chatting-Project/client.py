import socket
import threading
import pygame

# 클라이언트 설정
HOST = '127.0.0.1'
PORT = 12345

# Pygame 초기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Chat Client")

# 시스템 폰트 경로를 사용하여 한글 폰트 로드
font_path = "/Users/pkd/Desktop/dev/2024_ESG_Mentoring/python/ch02-venv/src/font/Hana2-Bold.ttf"
font = pygame.font.Font(font_path, 24)
big_font = pygame.font.Font(font_path, 50)
medium_font = pygame.font.Font(font_path, 40)

# 색상 정의
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
my_chat_color = pygame.Color('green')
other_chat_color = pygame.Color('skyblue')
system_message_color = pygame.Color('yellow')
color = color_inactive

# 시작 화면 변수
show_start_screen = True
show_nickname_screen = False
chat_running = False

# 채팅 화면 변수
input_box = pygame.Rect(20, 340, 450, 40)  # 세로 크기 조정
button_box = pygame.Rect(480, 340, 90, 40)  # 세로 크기 조정
active = False
text = ''
chat_history = []
nickname = ''

# 화면에 표시할 최대 메시지 수
MAX_MESSAGES_ON_SCREEN = 10

# 서버로부터 메시지를 수신하는 함수
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_history.append(message)
            if len(chat_history) > 100:
                chat_history.pop(0)
        except:
            print("Connection lost")
            client.close()
            break

# 서버로 메시지를 보내는 함수
def send_message(client, msg):
    client.send(f"{nickname}: {msg}".encode('utf-8'))
    chat_history.append(f"me: {msg}")  # 본인의 채팅은 'me:'로 표시
    if len(chat_history) > 100:
        chat_history.pop(0)

# 서버에 연결하는 함수
def start_chat():
    global chat_running, client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    chat_running = True
    
    # 닉네임을 서버로 전송
    client.recv(1024)  # 'NICK' 메시지 수신
    client.send(nickname.encode('utf-8'))

    # 수신 스레드 시작
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

# 닉네임 설정 함수
def set_nickname():
    global show_nickname_screen, show_start_screen
    show_start_screen = False
    show_nickname_screen = True

# 채팅 기록을 화면에 그리는 함수
def draw_chat_history():
    start_y = 20
    visible_history = chat_history[-MAX_MESSAGES_ON_SCREEN:]  # 화면에 보이는 최신 메시지들
    for i, msg in enumerate(visible_history):
        y_position = start_y + i * 30
        if msg.endswith("님이 들어오셨습니다.") or msg.endswith("님이 퇴장하셨습니다."):
            # 시스템 메시지 - 노란색
            txt_surface = font.render(msg, True, system_message_color)
            screen.blit(txt_surface, (20, y_position))
        elif msg.startswith("me:"):
            # 본인 메시지 - 녹색 오른쪽
            txt_surface = font.render(msg[4:], True, my_chat_color)
            screen.blit(txt_surface, (400, y_position))
        else:
            # 상대방 메시지 - 닉네임 포함 파란색 왼쪽
            txt_surface = font.render(msg, True, other_chat_color)
            screen.blit(txt_surface, (20, y_position))

# 메인 루프
running = True
while running:
    screen.fill((30, 30, 30))
    
    if show_start_screen:
        # 시작 화면 표시
        title_surface = big_font.render("인천상정고 / 하나금융TI", True, pygame.Color('white'))
        subtitle_surface = medium_font.render("(2024 ESG 멘토링)", True, pygame.Color('white'))
        start_button_surface = font.render("시작", True, pygame.Color('white'))
        title_rect = title_surface.get_rect(center=(300, 100))
        subtitle_rect = subtitle_surface.get_rect(center=(300, 180))
        start_button_rect = pygame.Rect(250, 250, 100, 50)
        
        # 화면에 텍스트와 버튼 배치
        screen.blit(title_surface, title_rect)
        screen.blit(subtitle_surface, subtitle_rect)
        pygame.draw.rect(screen, pygame.Color('dodgerblue2'), start_button_rect)
        screen.blit(start_button_surface, start_button_rect.move(25, 15))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    set_nickname()  # 닉네임 설정 화면으로 전환

    elif show_nickname_screen:
        # 닉네임 설정 화면 표시
        nickname_prompt_surface = medium_font.render("닉네임 입력       ", True, pygame.Color('white'))
        enter_button_surface = font.render("입장하기", True, pygame.Color('white'))
        nickname_rect = nickname_prompt_surface.get_rect(center=(350, 100))
        enter_button_rect = pygame.Rect(250, 250, 100, 50)
        nickname_input_box = pygame.Rect(100, 150, 400, 50)
        
        # 화면에 텍스트와 입력창, 버튼 배치
        screen.blit(nickname_prompt_surface, nickname_rect)
        pygame.draw.rect(screen, color_inactive, nickname_input_box)
        pygame.draw.rect(screen, pygame.Color('dodgerblue2'), enter_button_rect)
        screen.blit(enter_button_surface, enter_button_rect.move(15, 15))
        
        nickname_surface = font.render(nickname, True, pygame.Color('black'))
        screen.blit(nickname_surface, (nickname_input_box.x + 5, nickname_input_box.y + 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_nickname_screen = False
                    start_chat()  # 채팅 시작
                elif event.key == pygame.K_BACKSPACE:
                    nickname = nickname[:-1]
                else:
                    nickname += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if enter_button_rect.collidepoint(event.pos):
                    show_nickname_screen = False
                    start_chat()  # 채팅 시작

    elif chat_running:
        # 채팅 화면 표시
        draw_chat_history()

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        # 보내기 버튼
        send_button_surface = font.render("보내기", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('dodgerblue2'), button_box)
        screen.blit(send_button_surface, button_box.move(10, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                if button_box.collidepoint(event.pos) and text:
                    send_message(client, text)
                    text = ''
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN and text:
                        send_message(client, text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

    pygame.display.flip()
pygame.quit()
if chat_running:
    client.close()
