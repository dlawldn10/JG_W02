import sys
input = sys.stdin.readline

string = input().strip()

stack = []
answer = ''

def isVPS (str):
    stack = []
    for i in range (len(str)):
        if str[i] == "(" : stack.append( "(" )
        elif str[i] == "[" : stack.append( "[" )
        else : 
            if len(stack) == 0: return "NO"
            else : stack.pop()
    if len(stack) == 0: return "YES"
    else: return "NO"

if isVPS(string) == "YES":
    for i in string:
        stack.append(i)

        if len(stack) >= 2:
            if (stack[-2] == '(' and (stack[-1] == '(' or stack[-1] == '[')) or (stack[-2] == '[' and (stack[-1] == '(' or stack[-1] == '[')):  # left left
                answer += '('
            elif stack[-2] == '(' and stack[-1] == ')':  # left right
                answer += '2'
            elif stack[-2] == '[' and stack[-1] == ']':
                answer += '3'
            elif (stack[-2] == '(' and stack[-1] == ']') or (stack[-2] == '[' and stack[-1] == ')'):
                answer = '0'
                break
            elif (stack[-2] == ')' and (stack[-1] == '(' or stack[-1] == '[')) or (stack[-2] == ']' and (stack[-1] == '(' or stack[-1] == '[')):  # right left
                answer += '+'
            elif (stack[-2] == ']' and stack[-1] == ')') or (stack[-2] == ')' and stack[-1] == ')'):  # right right
                answer += ')*2'
            elif (stack[-2] == ']' and stack[-1] == ']') or (stack[-2] == ')' and stack[-1] == ']'):
                answer += ')*3'
else:
    answer = '0'
print(eval(answer))
