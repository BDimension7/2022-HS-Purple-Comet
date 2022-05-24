al = []
bl = []
cl = []

for a in range(200):
    for b in range(200):
        for c in range(200):
            if a ** 3 - b ** 3 - c ** 3 - a * b * c + 1 == 2022:
                al.append(a)
                bl.append(b)
                cl.append(c)
                if c == 2:
                    print(a, b, c)
print(min(al))
print(min(bl))
print(min(cl))
