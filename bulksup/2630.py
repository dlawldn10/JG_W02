import sys
input = sys.stdin.readline

length = int(input())

paper = []
for _ in range(length):
    paper.append(list(map(int, input().split())))


def cutting(x, y, len):
    global blue, white
    sum = 0

    for i in range(x, x+len):
        for j in range(y, y+len):
            sum += paper[i][j]

    if sum == len**2:
        blue += 1
    elif sum == 0:
        white += 1
    else:
        len = len // 2
        cutting(x, y, len)
        cutting(x+len, y, len)
        cutting(x, y+len, len)
        cutting(x+len, y+len, len)

blue = 0 
white = 0
cutting(0, 0, length)


print(white)
print(blue)
