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
        print(arr[0])


computar(12, 2)
