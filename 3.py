n = int(input("Введите число"))
t = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        t -= i
    if i % 2 != 0:
        t += i
        print(t)
