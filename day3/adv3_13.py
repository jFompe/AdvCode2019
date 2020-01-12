N = 9999
fich = "input3"

f = open(fich, "r")
row1 = f.readline().split(",")
row2 = f.readline().split(",")
f.close()

rows = [row1, row2]
sets = [set(), set()]
c = int((N-1)/2)

for row in [1,2]:
    i = c
    j = c
    for inst in rows[row-1]:
        dir = inst[0]
        dist = int(inst[1:])

        for n in range(dist):
            if dir == 'U':
                i-=1
            if dir == 'D':
                i+=1
            if dir == 'R':
                j+=1
            if dir == 'L':
                j-=1
            sets[row-1].add((i,j))

cortes = sets[0].intersection(sets[1])

min = N
for p in cortes:
    dist = abs((c-p[0])) + abs((c-p[1]))
    if dist < min:
        min = dist
print(min)
