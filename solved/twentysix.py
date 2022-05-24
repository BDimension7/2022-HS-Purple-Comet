import random


def status(arr):
    for i in range(len(arr) - 3):
        if arr[i] == 0 and arr[i + 1] == 0 and arr[i + 2] == 1 and arr[i + 3] == 0:
            return True
        elif arr[i] == 1 and arr[i + 1] == 0 and arr[i + 2] == 0 and arr[i + 3] == 1:
            return False


total = 0
won = 0


for _ in range(1000000):
    a = []
    while True:
        a.append(random.randint(0, 1))
        if len(a) > 3:
            if status(a):
                # print(a)
                won += 1
                total += 1
                break
            else:
                # print(a)
                total += 1
                break
    # print("game")
print(won / total)
