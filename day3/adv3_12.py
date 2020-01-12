N = 7001
fich = "input3"

mat = [[set() for x in range(N)] for y in range(N)]
# for r in mat:
#     print(r)


f = open(fich, "r")
row1 = f.readline().split(",")
row2 = f.readline().split(",")
f.close()

rows = [row1, row2]

c = int((N-1)/2)

for r in [1,2]:
    i = c
    j = c

    row = rows[r-1]

    for inst in row:
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
            mat[i][j].add(r)

# for r in mat:
#     print(r)

for i in range(N):
    for j in range(N):
        if len(mat[i][j]) == 2:
            print(str(i)+","+str(j))
