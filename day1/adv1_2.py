def fuel(num):
    return num/3 - 2

def module_fuel(mass):
    total = 0
    while (mass > 6):
        mass = fuel(mass)
        total += mass
    return total

with open("input1") as file:
    total = 0
    for n in file.readlines():
        total += module_fuel(int(n))
    print total
