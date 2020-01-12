N = 9


mat = []
row = []
for i in range(N):
    row.append(set())
for i in range(N):
    mat.append(row)
for r in mat:
    print(r)


f = open("input3", "r")
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
        num = int(inst[1:])

        if dir == 'U':
            for n in range(num):
                j+=1
                mat[i][j].add(r)
        if dir == 'D':
            for n in range(num):
                j-=1
                mat[i][j].add(r)
        if dir == 'L':
            for n in range(num):
                i-=1
                mat[i][j].add(r)
        if dir == 'R':
            for n in range(num):
                i+=1
                mat[i][j].add(r)




for i in range(N):
    for j in range(N):
        if len(mat[i][j]) == 2:
            #print(mat[i][j])
            print(str(i)+","+str(j))
