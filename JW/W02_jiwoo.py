# #1920
# N = int(input())
# a = sorted(list(map(int, input().split())))
# M = int(input())
# b = list(map(int, input().split()))

# for i in b:
#     isFound = False
#     left = 0
#     right = len(a)-1
#     mid = (left + right) // 2
#     while left <= right:
#         if a[mid] == i:
#             isFound = True
#             break

#         elif a[mid] > i:
#             right = mid - 1
#         else:
#             left = mid +1

#         mid = (left+right)//2

#     if isFound:
#         print(1)
#     else:
#         print(0)


# #2805
# N, M = map(int, input().split())
# h = list(map(int, input().split()))


# bottom = 1
# top = max(h)
# mid = (bottom + top)//2
# ans = 0

# while bottom <= top:
#     sum = 0
#     for height in h:
#         if height > mid:
#             sum += height - mid
#     # print(sum)
#     if sum < M:
#         top = mid - 1
#     elif sum >= M:
#         ans = mid
#         bottom = mid + 1
        

#     mid = (bottom + top)//2
#     # print(mid)

# print(mid)


# #2110
# import sys
# input = sys.stdin.readline
# N, C = map(int, input().split())

# house = []
# for _ in range(N):
#     house.append(int(input()))

# house.sort()

# start = 1
# end = house[-1] - house[0]
# mid = (start+end)//2

# while start <= end:
#     current = house[0]
#     count = 1
#     for i in range(1, len(house)):
#         if house[i] >= current + mid:
#             current = house[i]
#             count += 1

#     if count >= C:
#         #늘리기
#         start = mid + 1
#     elif count < C:
#         #줄이기
#         end = mid - 1

#     mid = (start + end) // 2
# print(mid)


# #2470
# #이분탐색으로 접근
# # pypy 통과
# import sys
# input = sys.stdin.readline
# N = int(input())
# l = list(map(int, input().split()))

# l.sort()
# ans = []
# min_sub = sys.maxsize
# for i in range(0, len(l)):
#     start = i
#     end = len(l)-1
#     mid = (start+end)//2
#     while start <= end:

#         if l[i] + l[mid] <= 0:
#             start = mid + 1

#         elif l[i] + l[mid] > 0:
#             end = mid - 1

#         mid = (start+end)//2

        
#         if abs(l[i] + l[mid]) <= min_sub and l[i] != l[mid]:
#             min_sub = abs(l[i] + l[mid])
#             ans.append((min_sub, sorted([l[i], l[mid]])))

# print(*sorted(ans)[0][1])


# #투포인터로 접근
# # input 입력 받기
# n = int(input())
# solution = list(map(int, input().split(' ')))

# # 정렬하기
# solution.sort()

# # 이중포인터 설정
# left = 0
# right = n-1

# answer = 2e+9+1 # 기준값
# final = [] # 정답

# # 투포인터 진행
# while left < right:
#     s_left = solution[left]
#     s_right = solution[right]

#     tot = s_left + s_right
#     # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
#     if abs(tot) < answer:
#         answer = abs(tot)
#         final = [s_left, s_right]
	
#     # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
#     if tot < 0:
#         left += 1
#     # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
#     else:
#         right -= 1

# print(final[0], final[1])


# #16564
# #4:14
# #4:53
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# l = []
# for _ in range(N):
#     l.append(int(input()))

# start = 1
# end = 10000000000
# mid = (start+end)//2

# while start <= end:
#     sum = 0
#     for lv in l:
#         if lv < mid:
#             sum += (mid-lv)

#     if sum > K:
#         end = mid - 1
#     elif sum <= K:
#         start = mid + 1

#     mid = (start+end)//2

# print(mid)


# #8983
# #정답코드 100점
# #나중에 다시 보기
# import sys
# input = sys.stdin.readline

# m, n, l = map(int, input().split())
# man = list(map(int, input().split()))
# man.sort()
# ani = [list(map(int, input().split())) for i in range(n)]

# cnt = 0
# for a,b in ani:
#     start = 0
#     end = len(man)-1
#     while start<end:
#         mid = (start+end)//2
#         if man[mid] < a:
#             start = mid+1
#         else:
#             end = mid
#     if abs(man[end]-a)+b<=l or abs(man[end-1]-a)+b<=l:
#         cnt += 1

# print(cnt)


# #60점
# import sys
# input = sys.stdin.readline
# M, N, L = map(int, input().split())
# Ms = list(map(int, input().split()))
# animals = []
# for _ in range(N):
#     animals.append(list(map(int, input().split())))

# count = 0
# killed = [0]*N
# for j in range(0, len(Ms)):
#     for i in range(0, len(animals)):
        
#         if animals[i][0] <= Ms[j]:
#             if  (animals[i][1] <= animals[i][0] + (L-Ms[j])) and (killed[i] == 0):
#                 #사정거리 안에 있으면
#                 count += 1
#                 killed[i] = 1 
#         else:
#             if  (animals[i][1] <= -animals[i][0] + (L+Ms[j])) and (killed[i] == 0):
#                 #사정거리 안에 있으면
#                 count += 1
#                 killed[i] = 1 

# print(count)



#2630
# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# result = []

# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)


# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))


# #1629
# def power(a, b):
#     if b == 1: # b의 값이 1이면 a % C를 return한다.
#         return a % C
#     else:
#         temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
#         if b % 2 == 0:
#             return temp * temp % C # b가 짝수인 경우
#         else:
#             return temp * temp * a % C # b가 홀수인 경우


# A, B, C = map(int, input().split())

# result = power(A, B)
# print(result)


# #10930
# #행렬 관련 다시 보기
# def mul(n, matrix1, matrix2):
#     result = [[0 for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 result[i][j] += matrix1[i][k]*matrix2[k][j]
#             result[i][j] %= 1000
#     return result

# def divide(n, b, matrix):
#     if b == 1: # b의 값이 1이면 a % C를 return한다.
#         return matrix
#     elif b == 2:
#         return mul(n, matrix, matrix)
#     else:
#         temp = divide(n, b // 2, matrix) # a^(b // 2)를 미리 구한다.
#         if b % 2 == 0:
#             return mul(n, temp, temp) # b가 짝수인 경우
#         else:
#             return mul(n, mul(n, temp, temp), matrix) # b가 홀수인 경우


# n, b = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]

# result = divide(n,b,a)
# for row in result:
#     for num in row:
#         print(num%1000, end=' ')
#     print()
        


# #2261
# #나중에 다시보기...
# n = int(input())
# coord = [list(map(int, input().split())) for _ in range(n)]


# #10828
# import sys
# input = sys.stdin.readline
# N = int(input())
# stk = []
# for _ in range(N):
#     cmd = input().split()

#     if cmd[0] == 'push':
#         stk.append(cmd[1])
#     elif cmd[0] == 'pop':
#         if len(stk) > 0:
#             print(stk.pop())
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(stk))
#     elif cmd[0] == 'empty':
#         if len(stk) > 0:
#             print(0)
#         else:
#             print(1)
#     elif cmd[0] == 'top':
#         if len(stk) > 0:
#             print(stk[-1])
#         else:
#             print(-1)


# #10773
# #11:31
# #11:36
# import sys
# input = sys.stdin.readline
# K = int(input())
# nums = []

# for _ in range(K):
#     a = int(input())
#     if a == 0:
#         nums.pop()
#     else:
#         nums.append(a)

# print(sum(nums))


# #9012
# T = int(input())

# for _ in range(T):
#     A = input()
#     stk = []
#     for a in A:
#         if a == '(':
#             stk.append('(')
#         else:
#             if len(stk) > 0:
#                 stk.pop()
#             else:
#                 stk.append(')')
#                 break


#     if len(stk) > 0:
#         print('NO')
#     else:
#         print('YES')


# #17608
# #pypy3 통과
# import sys
# input = sys.stdin.readline
# N = int(input())
# stk = []
# tmp = 0
# for i in range(0, N):
#     a = int(input())
#     #작아지는 경우 -> 스택에 담기
#     if len(stk) == 0:
#         stk.append(a)
#         tmp = a
#     else:
#         if tmp > a:
#             stk.append(a)
#             tmp = a
#         elif tmp <= a:
#             while True:
#                 stk.pop()
#                 if len(stk) == 0 or stk[-1] > a:
#                     break
#                 tmp = stk[-1]
#             stk.append(a)
#             tmp = a
    

# print(len(stk))
# # print(stk)


# # #다른 풀이
# # import sys
# # input = sys.stdin.readline

# # n = int(input())
# # l = []

# # for _ in range(n):
# # 	l.append(int(input()))
# # count = 0
# # max = 0
# # for x in reversed(l):
# # 	if max < x:
# # 		max = x
# # 		count += 1
# # print(count)


#2504
#계산만 잘하면 될거같은데...
# L = input()
# stk1 = []
# stk2 = []
# isOpen = True
# tmp = ''
# def check():
#     global tmp

#     if (len(stk1) == 1 and len(stk2) == 0) or (len(stk1) == 0 and len(stk2) == 1) or (len(stk1) == 0 and len(stk2) == 0):
#         print(tmp)
#         tmp = str(eval(tmp))
#         return True
#     else:
#         return False

# for l in L:

#     if isOpen:
#         if l == '(':
#             stk1.append('(')
#             isOpen = True
#         elif l == '[':
#             stk2.append('[')
#             isOpen = True
#         elif l == ')' and len(stk1) > 0:
#             stk1.pop()
#             tmp += '2'
#             isOpen = False
#         elif l == ']' and len(stk2) > 0:
#             stk2.pop()
#             tmp += '3'
#             isOpen = False
#         else:
#             tmp = 0
#             break

#     else:
#         if l == '(':
#             stk1.append('(')
#             tmp += '+'
#             isOpen = True
#         elif l == '[':
#             stk2.append('[')
#             tmp += '+'
#             isOpen = True
#         elif l == ')' and len(stk1) > 0:
#             stk1.pop()
#             check()
#             tmp += '*'
#             tmp += '2'
#             isOpen = False
            
#         elif l == ']' and len(stk2) > 0:
#             stk2.pop()
#             check()
#             tmp += '*'
#             tmp += '3'
#             isOpen = False
            
#         else:
#             tmp = 0
#             break
    
    
# print(str(eval))
# # print(eval(tmp))


# #정답 코드
# s = input()
# stack = []
# tmp = 1
# res = 0

# # for c in s를 하면 안 되고 길이로 돌아야 함
# for i in range(len(s)):
#   if s[i] == '(':
#     tmp *= 2
#     stack.append(s[i])
#   elif s[i] == '[':
#     tmp *= 3
#     stack.append(s[i])

#   elif s[i] == ')':
#     if not stack or stack[-1] == '[':
#       res = 0
#       break
#     if s[i-1] == '(':
#       res += tmp
#     tmp //= 2
#     stack.pop() # pop도 까먹지 말고 꼭
  
#   else:
#     if not stack or stack[-1] == '(':
#       res = 0
#       break
#     # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
#     # 단, 이 경우는 오류는 아님
#     if s[i-1] == '[':
#       res += tmp
#     tmp //= 3
#     stack.pop() # pop 까먹지 말기

# if stack:
#   res = 0
# print(res)



# #2493
# import sys
# input = sys.stdin.readline

# n = int(input())
# t_list = list(map(int, input().split()))
# stk = []

# for i in range(n):
#     h = t_list[i]
#     if stk:
#         #원소가 있을 때
#         while stk:
#             if stk[-1][0] > h:
#                 print(stk[-1][1]+1, end=' ')
#                 break
#             elif stk[-1][0] < h:
#                 #이전것은 pop한다.
#                 stk.pop()
#                 if not stk:
#                     print(0, end=' ')
#             else:
#                 print(stk[-1][1]+1, end=' ')
#                 stk.pop()
#                 break

#         #새로운거 넣기
#         stk.append([h, i])

#     else:
#         #원소가 없을때
#         print(0, end=' ')
#         stk.append([h, i])



#2812
N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while stack and K > 0 and stack[-1] < num[i]:
        stack.pop()
        K -= 1
    stack.append(num[i])

print(''.join(stack[:N-K]))

