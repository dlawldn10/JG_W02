import sys

n = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))

array1.sort()

# arr2에 있는 수들이 arr1에 존재 하는지

for i in range(m):
    pl = 0
    pr = n-1
    key = array2[i]
    while True:
        pc = (pl + pr) // 2
        if array1[pc] == key:
            print(1)
            break
        elif array1[pc] < key:
            pl = pc + 1
        else:
            # array1[pc] > key:
            pr = pc - 1
        if pl > pr:
            print(0)
            break

    

    
