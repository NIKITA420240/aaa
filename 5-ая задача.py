def f(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return 0
        d += 1
    return 1

mas = []
for i in range(10000):
    x = f(i + 1)
    if x == 1:
        mas.append(i + 1)
print(mas)

for i in range(3,10000,2):
    flag = False
    if i not in mas:
        for j in range(len(mas)):
            a = mas[j]
            b = (i - a)
            if (b > 0) and (b % 2 == 0):
                z = b // 2
                if (z ** 0.5) == int(z ** 0.5):
                    flag = True
        if flag == False:
            print(i)
            break
