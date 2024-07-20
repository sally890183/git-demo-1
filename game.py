import random

x = random.randint(1, 50)

print(x)

for i in range(5):
    y = int(input("請猜一個數字："))
    if y == x:
        print("答對了!")
        break
    else:
        if x > y:
            print(f"搭搭，答錯！猜高一點")
        else:
            print(f"搭搭，答錯！猜低一點")
if x != y:
    print(f"機會用完! 正確答案為：{x}")
print("123545")
