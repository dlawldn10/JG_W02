from collections import deque
import sys
input = sys.stdin.readline

while True:
    rectan = list(map(int, input().split()))
    n = rectan.pop()

    if n == 0:
        break

    stack = deque()
    answer = 0

    for i in range(n):
        while len(stack) != 0 and rectan[stack[-1]] > rectan[i]:
            temp = stack.pop()

            if len(stack) == 0:
                width = 1
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * rectan[temp])
        stack.append[i]

    while len(stack) != 0:
        temp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * rectan[temp])

    print(answer)
