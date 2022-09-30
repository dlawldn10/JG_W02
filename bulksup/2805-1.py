import sys

number_tree, key = map(int, sys.stdin.readline().split())
list_tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(list_tree)

while start <= end:
    mid = (start + end)//2
   
    sum = 0

    for i in list_tree:
        if i >= mid:
            sum += i - mid
    if sum >= key:
        start = mid+1
    else:
        end = mid-1
print(end)
