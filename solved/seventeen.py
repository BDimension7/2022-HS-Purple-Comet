def reverse(n):
    n = str(n)
    s = ""
    for i in range(len(n) - 1, -1, -1):
        s += n[i]
    return int(s)


n = 1

while True:
    if reverse(n) + 450 == n:
        print(n)
        break
    n += 1
