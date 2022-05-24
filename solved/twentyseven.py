def kfunc(k):
    sum = 0
    for i in range(1, k + 1):
        sum += i / (4 * (i ** 4) + 1)
    return sum


n = 1
while True:
    if kfunc(n) > 505.45 / 2022:
        print(n)
        break
    n += 1


print(n)
print(kfunc(71) > 505.45 / 2022)
