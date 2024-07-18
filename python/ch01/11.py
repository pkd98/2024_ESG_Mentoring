numbers = [1, 2, 3, 4, 5]

# 요소 추가
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# 요소 삽입
numbers.insert(2, 2.5)
print(numbers)  # [1, 2, 2.5, 3, 4, 5, 6]

# 요소 제거
numbers.pop(3)
print(numbers)  # [1, 2, 2.5, 4, 5, 6]

# 리스트 정렬
numbers.sort()
print(numbers)  # [1, 2, 2.5, 4, 5, 6]

# 리스트 반전
numbers.reverse()
print(numbers)  # [6, 5, 4, 2.5, 2, 1]