def fuel(num):
    return num/3 - 2

with open("input1") as file:
    total = 0
    for n in file.readlines():
        total += fuel(int(n))
    print total
