# 리스트 생성
fruits = ["apple", "banana", "cherry"]

# 리스트 요소 접근
print(fruits[0])  # apple

# 리스트 요소 변경
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# 리스트에 요소 추가
fruits.append("orange")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'orange']

# 리스트에서 요소 제거
fruits.remove("apple")
print(fruits)  # ['blueberry', 'cherry', 'orange']

# 리스트 길이 확인
print(len(fruits))  # 3