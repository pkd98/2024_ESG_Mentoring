import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 연합뉴스 메인 페이지 URL
url = "https://www.yna.co.kr/"

# 요청 헤더 설정 (User-Agent)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# 페이지 요청 및 HTML 가져오기
response = requests.get(url, headers=headers)

# 페이지 파싱
soup = BeautifulSoup(response.content, 'html.parser')

# 뉴스 제목들 수집
titles = []
# class="tit-news"로 지정된 뉴스 제목 추출
for item in soup.find_all(class_='tit-news'):
    title = item.get_text().strip()
    if title:
        titles.append(title)

# 제목들을 하나의 문자열로 결합
text = ' '.join(titles)

# 크롤링된 제목 확인
if text:
    print("크롤링된 뉴스 제목:")
    print(text)
else:
    print("No text found to generate a word cloud.")

# 워드클라우드 생성
if text:
    wordcloud = WordCloud(font_path='/Users/pkd/Desktop/dev/2024_ESG_Mentoring/python/ch02-venv/src/font/Hana2-Bold.ttf', background_color='white', width=800, height=400).generate(text)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
