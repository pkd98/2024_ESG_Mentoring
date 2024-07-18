# 집합 생성
fruits_set = {"apple", "banana", "cherry"}

# 집합에 요소 추가
fruits_set.add("orange")
print(fruits_set)  # {'apple', 'banana', 'cherry', 'orange'}

# 집합에서 요소 제거
fruits_set.remove("banana")
print(fruits_set)  # {'apple', 'cherry', 'orange'}

# 집합 간의 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
print(set1 | set2)  # {1, 2, 3, 4, 5}

# 교집합
print(set1 & set2)  # {3}

# 차집합
print(set1 - set2)  # {1, 2}

# 대칭 차집합
print(set1 ^ set2)  # {1, 2, 4, 5}