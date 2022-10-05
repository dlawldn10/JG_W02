from collections import deque
import sys
input = sys.stdin.readline

length_map = int(input())
number_apple = int(input())
list_apple = []
for _ in range(number_apple):
    x, y = map(int, input().split())
    list_apple.append((x-1, y-1))

number_turn = int(input())

list_turn = []
for _ in range(number_turn):
    after_second, left_right = map(str, input().split())
    list_turn.append((int(after_second), left_right))

que_snake = deque([(0, 0)])
second = 0
direction = deque(['right', 'down', 'left', 'up'])
while 0 <= que_snake[-1][0] < length_map and 0 <= que_snake[-1][1] < length_map:
    second += 1
    if direction[0] == 'right':
        que_snake.append((que_snake[-1][0], que_snake[-1][1] + 1))
    elif direction[0] == 'down':
        que_snake.append((que_snake[-1][0]+1, que_snake[-1][1]))
    elif direction[0] == 'left':
        que_snake.append((que_snake[-1][0], que_snake[-1][1]-1))
    elif direction[0] == 'up':
        que_snake.append((que_snake[-1][0]-1, que_snake[-1][1]))

    if que_snake.count(que_snake[-1]) == 2:
        break
    
    if (que_snake[-1][0], que_snake[-1][1]) not in list_apple:
        que_snake.popleft()
    else:
        list_apple.remove((que_snake[-1][0], que_snake[-1][1]))
    for i,j in list_turn:
        if i == second:
            if j == 'D':
                direction.rotate(-1)
            elif j == 'L':
                direction.rotate(+1) 
                
print(second)
