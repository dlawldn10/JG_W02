# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

# 예제 입력 1
# 2 5
# 1 2
# 3 4
# 예제 출력 1
# 69 558
# 337 406
# 예제 입력 2
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 예제 출력 2
# 468 576 684
# 62 305 548
# 656 34 412
# 예제 입력 3
# 5 10
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 예제 출력 3
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512

import sys
input = sys.stdin.readline

length, squared = map(int, input().split())

matrix = []
for _ in range(length):
    row = list(map(int, input().split()))
    matrix.append(row)


def calculate(mrx1, mrx2):
    matrix_calculated = [[]] * length

    for i in range(length):
        matrix_calculated[i] = [0] * length
        for j in range(length):
            for k in range(length):
                matrix_calculated[i][j] += mrx1[i][k]*mrx2[k][j]
            matrix_calculated[i][j] = matrix_calculated[i][j] % 1000
    return matrix_calculated


def matrix_multiply(mrx, sqr):
    if sqr == 1:
        for i in range(len(mrx)):
            for j in range(len(mrx)):
                mrx[i][j] %= 1000
        return mrx
    else:
        res = matrix_multiply(mrx, sqr//2)
        if sqr % 2 == 0:
            return calculate(res, res)
        else:
            return calculate(calculate(res, res), mrx)


answer = matrix_multiply(matrix, squared)
for i in answer:
    print(*i)
