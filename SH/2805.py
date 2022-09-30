# https://claude-u.tistory.com/446
import sys

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2 # 단위 : 정수

    log_sum = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid: # 길이가 기준보다 높은 나무만 잘림
            log_sum += i - mid

    #벌목 높이를 이분탐색, 기준 M
    if log_sum >= M:
        start = mid + 1 

    else:
        end = mid - 1

print(end)

