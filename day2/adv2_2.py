def show(array):
    for n in array:
        print(str(n)+',', end = '')
    print()

def computar(a, b):
    with open("input2") as file:
        data = file.readline()
        arr = []
        for num in data.split(','):
            arr.append(int(num))
        arr[1] = a
        arr[2] = b
        i = 0
        n = arr[i]
        while n != 99:
            n = arr[i]
            if n == 1:
                arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
            if n == 2:
                arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
            i += 4
        return(arr[0])

# FUERZA BRUTA
for i in range(0, 100):
    for j in range(0, 100):
        if computar(i, j) == 19690720:
            print(i)
            print(j)
            exit()
