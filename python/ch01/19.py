x = 10  # 전역 변수

def local_scope():
    x = 5  # 지역 변수
    print(x)  # 5 출력

def change_global():
    global x
    x = 5


local_scope()
print(x)  # 10 출력

change_global()
print(x)  # 5 출력