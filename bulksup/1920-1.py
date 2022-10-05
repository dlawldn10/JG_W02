import sys

number_exist_figure = int(sys.stdin.readline())
list_exist_figure = list(map(int, sys.stdin.readline().split()))
list_exist_figure.sort()
number_key_figure = int(sys.stdin.readline())
list_key_figure = list(map(int, sys.stdin.readline().split()))



def indexing(list, key):
    start = 0
    end = len(list)-1
    mid = (start+end)//2
    isFound = False
    while start <= end:
        if list[mid] == key:
            isFound = True
            break
        elif list[mid] < key:
            start = mid+1

        elif list[mid] > key:
            end = mid-1

        mid = (start+end)//2
    if isFound == True:
        print(1)
    else:
        print(0)    

for i in list_key_figure:
    indexing(list_exist_figure,i) 
