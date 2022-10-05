import sys
input = sys.stdin.readline

number_stick = int(input())
stack_stick = []
for _ in range(number_stick):
    stack_stick.append(int(input()))

maximum_height = 0
result = 0

for i in range(number_stick-1, -1, -1):
    if stack_stick[i] > maximum_height :
        result += 1
        maximum_height = stack_stick[i]

print(result)
