# 문제
# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

# 예제 입력 1
# 4 2
# 1924
# 예제 출력 1
# 94
# 예제 입력 2
# 7 3
# 1231234
# 예제 출력 2
# 3234
# 예제 입력 3
# 10 4
# 4177252841
# 예제 출력 3
# 775841

import sys
input = sys.stdin.readline

number_figure, number_delete = map(int, input().split())
list_figure = list(input().strip())
k, stack = number_delete, []

for i in range(number_figure):
    while k > 0 and stack and stack[-1] < list_figure[i]:
        stack.pop()
        k -= 1
    stack.append(list_figure[i])

print(''.join(stack[:number_figure-number_delete]))
