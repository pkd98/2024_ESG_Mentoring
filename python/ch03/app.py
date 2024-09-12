from flask import Flask, render_template, Response, request
import pygame
import io
import threading
from PIL import Image

app = Flask(__name__)

# 전역 변수 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.Surface((WIDTH, HEIGHT))  # 디스플레이 표면 대신 사용
clock = pygame.time.Clock()
running = True

# Pygame 초기화
pygame.init()

# 게임 로직 (간단한 예제)
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

def game_loop():
    global running, player_x, player_y, screen
    while running:
        screen.fill((0, 0, 0))  # 화면 초기화
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))

        clock.tick(60)

@app.route('/')
def index():
    return render_template('index.html')

def generate_video_feed():
    global screen
    while True:
        try:
            # Pygame 화면을 이미지로 변환
            pil_string_image = pygame.image.tostring(screen, "RGB")
            pil_image = Image.frombytes("RGB", (WIDTH, HEIGHT), pil_string_image)
            
            # 이미지 스트림
            img_io = io.BytesIO()
            pil_image.save(img_io, 'JPEG')
            img_io.seek(0)

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_io.read() + b'\r\n')
        except Exception as e:
            print(f"Error generating video feed: {e}")

@app.route('/video_feed')
def video_feed():
    return Response(generate_video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/keypress', methods=['POST'])
def keypress():
    try:
        key = request.form['key']
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=key))
        return '', 204
    except Exception as e:
        print(f"Error handling keypress: {e}")
        return '', 500

if __name__ == '__main__':
    game_thread = threading.Thread(target=game_loop)
    game_thread.start()
    
    # Flask 서버 실행 (포트를 5001로 변경)
    app.run(host='0.0.0.0', port=5001, debug=True)

    running = False
    game_thread.join()
    pygame.quit()

