# 딕셔너리 생성
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"]
}

# 딕셔너리 요소 접근
print(student["name"])  # John

# 딕셔너리 요소 추가 및 변경
student["age"] = 21
student["grade"] = "A"
print(student)  # {'name': 'John', 'age': 21, 'courses': ['Math', 'Science'], 'grade': 'A'}

# 딕셔너리 요소 제거
del student["courses"]
print(student)  # {'name': 'John', 'age': 21, 'grade': 'A'}

# 딕셔너리 키 목록
print(student.keys())  # dict_keys(['name', 'age', 'grade'])

# 딕셔너리 값 목록
print(student.values())  # dict_values(['John', 21, 'A'])

# 딕셔너리 키-값 쌍 목록
print(student.items())  # dict_items([('name', 'John'), ('age', 21), ('grade', 'A']))

# 딕셔너리 요소 가져오기 (기본값 지정)
print(student.get("courses", "Not enrolled"))  # Not enrolled