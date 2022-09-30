# https://claude-u.tistory.com/446
import sys

N, M = map(int, input().split())
tree = list(map(int, input().split()))
# 보통 이진 탐색에서 start와 end는 index
start, end = 1, max(tree) #이분탐색 검색 범위 설정, 처음부터 sum < M 으로 간다면 인덱스가 (-)가 된다.
# 왜 1 일까?

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2 # 단위 : 정수

    sum = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid: # 길이가 기준보다 높은 나무만 잘림
            sum += i - mid
    
    print('mid', mid)
    print(f'sum = {sum}')

    #벌목 높이를 이분탐색, 기준 M
    if sum > M: # sum = M 일 때가 없을 수 있다. 
        start = mid + 1 # 왜 1을 더할까? 역전될 수 있도록 하기 위해서 (index 이거나 양의 정수일 때)
        print('7 이상 start=', start, 'end=', end, '\n')

    elif sum == M:
        end = mid
        break

    #elif 지우고, sum >= M 을 하면 더 빠르다
    else:
        end = mid - 1 # 왜 1을 뺄까? 역전될 수 있도록 하기 위해서 (index 이거나 양의 정수일 때)
        print('7 미만 start=', start, 'end=', end, '\n')

print(end)

