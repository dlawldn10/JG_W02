# 원 영역 다국어

# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	1355	480	328	37.104%
# 문제
# x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.

# 원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.

# 영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.


# 입력
# 첫째 줄에 원의 개수 N(1 ≤ N ≤ 300,000)이 주어진다.

# 다음 N개 줄에는 각 원의 정보 xi와 ri가 정수로 주어진다. xi는 원의 중심 좌표이며, ri는 반지름이다. (-109 ≤ xi ≤ 109, 1 ≤ ri ≤ 109)

# 입력으로 주어지는 원은 항상 유일하다.

# 출력
# 첫째 줄에 원으로 인해서 만들어지는 영역의 개수를 출력한다.

# 예제 입력 1
# 2
# 1 3
# 5 1
# 예제 출력 1
# 3
# 예제 입력 2
# 3
# 2 2
# 1 1
# 3 1
# 예제 출력 2
# 5
# 예제 입력 3
# 4
# 7 5
# -9 11
# 11 9
# 0 20
# 예제 출력 3
# 6

import sys
input = sys.stdin.readline

number = int(input())

list_circles = []

for i in range(number):
    center, radius = map(int, input().split())
    list_circles.append((center - radius, '('))
    list_circles.append((center + radius, ')'))

list_circles = sorted(list_circles, key=lambda x: (x[0], -ord(x[1])))

stack = []

answer = 1

for i in range(number * 2):
    position, bracket = list_circles[i]
    if len(stack) == 0:
        stack.append({'pos': position, 'bracket': bracket, 'status': 0})
        continue

    if bracket == ')':
        if stack[-1]['status'] == 0:
            answer += 1
        elif stack[-1]['status'] == 1:
            answer += 2
        stack.pop()

        if i != number*2-1:
            if list_circles[i+1][0] != position:
                stack[-1]['status'] = 0
    else:
        if stack[-1]['pos'] == position:
            stack[-1]['status'] = 1
            stack.append({'pos': position, 'bracket': bracket, 'status': 0})
        else:
            stack.append({'pos': position, 'bracket': bracket, 'status': 0})

print(answer)
