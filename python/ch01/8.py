for i in range(10):
    if i == 5:
        break
    print(i)

print("--------------------")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("--------------------")

for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)