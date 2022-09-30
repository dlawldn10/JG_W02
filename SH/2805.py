# https://claude-u.tistory.com/446
from distutils.log import Log
import sys

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정
# 왜 1 일까?

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid: # 길이가 기준보다 높은 나무만 잘림
            log += i - mid
    
    print('mid', mid)
    print(f'log = {log}')

    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1 # 왜 1을 더할까?
        print('7 이상 start=', start, 'end=', end, '\n')
    else:
        end = mid - 1
        print('7 미만 start=', start, 'end=', end, '\n')

print(end)