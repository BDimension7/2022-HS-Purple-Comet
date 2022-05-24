days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
for y in range(2, 11):
    for m in range(1, 13):
        for d in range(days[m - 1]):
            if m * d == y + 20:
                print(m, d, y + 20)
                count += 1
print(count)
