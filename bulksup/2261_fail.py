# 문제
# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 여러 점이 같은 좌표를 가질 수도 있다.

# 출력
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.

# 예제 입력 1
# 4
# 0 0
# 10 10
# 0 10
# 10 0
# 예제 출력 1
# 100

import sys
input = sys.stdin.readline

number_point = int(input())

list_point = []
for _ in range (number_point):
    list_point.append(list(map(int, input().split())))

min = float('inf')
def distance_squared(list, n):
    global min
    if n == len(list)-1:
        return min
    else:
        for i in range(n+1, len(list)):
            distance = (list[i][0] - list[n][0])**2 + (list[i][1] - list[n][1])**2
            if distance < min:
                min = distance
        distance_squared(list, n+1)

distance_squared(list_point, 0)

print(min)