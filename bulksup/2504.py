import sys
input = sys.stdin.readline

string = input().strip()

temp = 1
stack = []
answer = 0

if len(string) == 1:
    answer = 0
else:
    for i in range(len(string)):
        letter = string[i]
        if letter == "(":                      # 1. 괄호 만드는 놈 (left )
            temp *= 2                          # 1.1 둥근 놈(숫자 2 미리 곱)
            stack.append(letter)
        elif letter == "[":                    # 1.2 네모난 놈(숫자3 미리 곱)
            temp *= 3
            stack.append(letter)
        elif letter == ")":                                       # 2. 괄호 닫는 놈 (right)
            if len(stack) == 0 or stack[-1] == "[":                 # 2.1 숫자 2 만드는 놈
                answer = 0
                break                   
            elif string[i-1] == "(":              
                answer += temp
                temp //= 2
                stack.pop()
            elif string[i-1] == ")" or string[i-1] == "]":
                temp //= 2
                stack.pop()
        elif letter == "]":
            if len(stack) == 0 or stack[-1] == "(":
                answer = 0
                break
            elif string[i-1] == "[":               # 2.2 숫자 3 만드는 놈
                answer += temp
                temp //= 3
                stack.pop()
            elif string[i-1] == ")" or string[i-1] == "]":
                temp //= 3
                stack.pop()


    if len(stack) != 0:
        answer = 0
print(answer)
