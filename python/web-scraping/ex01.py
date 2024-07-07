from bs4 import BeautifulSoup

# HTML 문서 예제
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')

# HTML 문서 예쁘게 출력
print(soup.prettify())

# 특정 요소 추출
print(soup.title)  # <title>The Dormouse's story</title>
print(soup.title.string)  # The Dormouse's story
print(soup.a)  # 첫 번째 <a> 태그: <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
print(soup.find_all('a'))  # 모든 <a> 태그 리스트

