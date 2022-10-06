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

# while bottom <= top:
#     sum = 0
#     for height in h:
#         if height > mid:
#             sum += height - mid
#     # print(sum)
#     if sum < M:
#         top = mid - 1
#     elif sum >= M:
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



# #2812
# N, K = map(int, input().split())
# num = list(input())
# k, stack = K, []

# for i in range(N):
#     while stack and K > 0 and stack[-1] < num[i]:
#         stack.pop()
#         K -= 1
#     stack.append(num[i])

# print(''.join(stack[:N-K]))


# #10000
# import sys
# input = sys.stdin.readline
# N = int(input())
# circles = []
# for _ in range(N):
#     point, radius = map(int, input().split())
#     circles.append((point-radius, '('))
#     circles.append((point+radius, ')'))

# #좌표 기준 정렬, 같은 좌표일 경우 ')'에게 우선순위
# circles = sorted(circles, key= lambda x:(x[0], -ord(x[1])))

# # print(circles)
# stk = []
# answer = 1
# for i in range(len(circles)):
#     position, bracket = circles[i] 
#     if len(stk) == 0:
#         stk.append({'pos': circles[i][0], 'bracket': circles[i][1], 'status': 0})
#         continue

#     #닫힌괄호 일때
#     if bracket == ')':
#         if stk[-1]['status'] == 0:
#             answer += 1
#         elif stk[-1]['status'] == 1:
#             answer += 2

#         stk.pop()

#         #원이 이어져있는지 확인
#         if i != len(circles)-1:
#             if circles[i+1][0] != position:
#                 stk[-1]['status'] = 0


#     #열린괄호 일때    
#     else:
#         if stk[-1]['pos'] == position:
#             #접하는 경우
#             stk[-1]['status'] = 1
#             stk.append({'pos': position, 'bracket': bracket, 'status': 0})
#         else:
#             #접하지 않음
#             stk.append({'pos': position, 'bracket': bracket, 'status': 0})
        
    
# print(answer)


# #18258
# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# dq = deque()
# for _ in range(N):
#     cmd = input().split()

#     if cmd[0] == 'push':
#         dq.append(cmd[1])
#     elif cmd[0] == 'pop':
#         if len(dq) > 0:
#             print(dq.popleft())
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(dq))
#     elif cmd[0] == 'empty':
#         if len(dq) > 0:
#             print(0)
#         else:
#             print(1)
#     elif cmd[0] == 'front':
#         if len(dq) > 0:
#             print(dq[0])
#         else:
#             print(-1)
#     elif cmd[0] == 'back':
#         if len(dq) > 0:
#             print(dq[-1])
#         else:
#             print(-1)



# #2164
# from collections import deque
# dq = deque([i for i in range(1, int(input())+1)])

# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq.popleft())


# #11866
# from collections import deque
# N, K = map(int, input().split())
# dq = deque([i for i in range(1, N+1)])

# print('<', end='')
# while len(dq) > 0:
#     for _ in range(K-1):
#         dq.append(dq.popleft())
    

#     if len(dq) == 1:
#         print(dq.popleft(), end='>')
#     else:
#         print(dq.popleft(), end=', ')


# #11297
# import sys, heapq
# input = sys.stdin.readline
# N = int(input())
# hq = []
# for _ in range(N):
#     num = int(input())
#     if num == 0:
#         print(abs(heapq.heappop(hq)) if len(hq)>0 else 0)
#     else:
#         heapq.heappush(hq, -num)


# #1655
# #시간초과
# # import sys, heapq, copy
# # input = sys.stdin.readline
# # N = int(input())
# # hq = []

# # for i in range(1, N+1):
# #     num = int(input())
# #     heapq.heappush(hq, num)
# #     tmp = copy.deepcopy(hq)
# #     # print(tmp)
# #     if i%2 == 0:
# #         for j in range(i//2-1):
# #             heapq.heappop(tmp)
# #     else:
# #         for j in range(i//2):
# #             heapq.heappop(tmp)
# #     print(heapq.heappop(tmp))


# #정답 코드
# #힙을 두개 쓰기
# #left는 최대힙, right는 최소힙
# import sys, heapq
# input = sys.stdin.readline
# N = int(input())
# left_hq = []
# right_hq = []
# answer = []

# for i in range(1, N+1):
#     num = int(input())

#     if len(left_hq) == len(right_hq):
#         heapq.heappush(left_hq, -num)
#     else:
#         heapq.heappush(right_hq, num)
    
#     if right_hq and right_hq[0] < -left_hq[0]:
#         print('-left0: ' + str(-left_hq[0]))
#         print('right0: ' + str(right_hq[0]))
#         leftValue = heapq.heappop(left_hq)
#         rightValue = heapq.heappop(right_hq) 

#         heapq.heappush(left_hq, -rightValue)
#         heapq.heappush(right_hq, -leftValue)

#     print(-left_hq[0])


# #1715
# import sys, heapq
# input = sys.stdin.readline
# N = int(input())
# card_deck = []

# for _ in range(N):
#     heapq.heappush(card_deck, int(input()))

# if len(card_deck) <= 1:
#     print(0)
# else:
#     answer = 0
#     while len(card_deck) > 1:
        
#         deck1 = heapq.heappop(card_deck)
#         deck2 = heapq.heappop(card_deck)
#         answer += deck1 + deck2
#         heapq.heappush(card_deck, deck1 + deck2)

#     print(answer)


# #13334
# import heapq, sys

# input = sys.stdin.readline

# n = int(input())
# points = []



# #3190
# from collections import deque
# import sys
# input = sys.stdin.readline
# length_map = int(input())
# number_apple = int(input())
# list_apple = []

# for _ in range(number_apple):
#     x, y = map(int, input().split())
#     list_apple.append((x-1, y-1))

# number_turn = int(input())
# list_turn = []

# for _ in range(number_turn):
#     after_second, left_right = map(str, input().split())
#     list_turn.append((int(after_second), left_right))

# que_snake = deque([(0, 0)])
# second = 0
# direction = deque(['right', 'down', 'left', 'up'])
# while 0 <= que_snake[-1][0] < length_map and 0 <= que_snake[-1][1] < length_map:
#     second += 1
#     if direction[0] == 'right':
#         que_snake.append((que_snake[-1][0], que_snake[-1][1] + 1))
#     elif direction[0] == 'down':
#         que_snake.append((que_snake[-1][0]+1, que_snake[-1][1]))
#     elif direction[0] == 'left':
#         que_snake.append((que_snake[-1][0], que_snake[-1][1]-1))
#     elif direction[0] == 'up':
#         que_snake.append((que_snake[-1][0]-1, que_snake[-1][1]))
#     if que_snake.count(que_snake[-1]) == 2:
#         break
#     if (que_snake[-1][0], que_snake[-1][1]) not in list_apple:
#         que_snake.popleft()
#     else:
#         list_apple.remove((que_snake[-1][0], que_snake[-1][1]))
#     for i,j in list_turn:
#         if i == second:
#             if j == 'D':
#                 direction.rotate(-1)
#             elif j == 'L':
#                 direction.rotate(+1)
# print(second)

    
#6549
# #시간초과
# import sys
# input = sys.stdin.readline

# while True:
#     l = list(map(int, input().split()))
#     n = l[0]
#     checked = []
#     if n == 0:
#         break
#     width = 1
#     max_area = 0
#     for i in range(1, len(l)):
#         pivot = l[i]
#         if pivot in checked:
#             continue

#         checked.append(l[i])
#         for j in range(1, len(l)):
#             if l[j] >= pivot and j !=len(l)-1:
#                 width += 1
#             else:
#                 max_area = max(width*pivot, max_area)
#                 # print(max_area)
#                 width = 0

#     print(max_area)


# #스택 사용 정답 코드
# import sys
# input = sys.stdin.readline

# while True:
#     n, *l = map(int, input().split())
    
#     if n == 0:
#         break
    
#     max_area = 0
#     stack = []

#     for i in range(0, len(l)):
#         idx = i
#         while stack and stack[-1][0] >= l[i]:
#             h, idx = stack.pop()
#             tmp = h * (i-idx)
#             max_area = max(max_area, tmp)

#         stack.append([l[i], idx])

#     for h, point in stack:
#         max_area = max(max_area, (n-point)*h)

#     print(max_area)



#################
##개인 Practice##
#################


# #10816
# #bisect 사용 풀이
# from bisect import bisect_right, bisect_left

# N = int(input())
# cards = sorted(list(map(int, input().split())))
# M = int(input())
# ans = []
# for i in map(int, input().split()):
#     ans.append(bisect_right(cards, i) - bisect_left(cards, i))

# print(' '.join(map(str, ans)))


# #map 사용 풀이
# N = int(input())
# cards = {}
# for num in map(int,input().split()):
#     if num in cards:
#         cards[num] += 1
#     else:
#         cards[num] = 1

# M = int(input())
# ans = []
# for i in map(int, input().split()):
#     if i in cards:
#         ans.append(cards[i])
#     else:
#         ans.append(0)

# print(' '.join(map(str, ans)))


# #11286
# import heapq, sys
# input = sys.stdin.readline
# N = int(input())
# hq = []
# for _ in range(N):
#     num = int(input())
#     if num != 0:
#         heapq.heappush(hq, (abs(num), num))
#     elif num == 0:
#         if len(hq) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(hq)[1])


# #5397
# T = int(input())

# for _ in range(T):
#     stk1 = []
#     stk2 = []
#     input_str = input()
#     for l in input_str:
#         if l == "<":
#             if len(stk1) > 0:
#                 stk2.append(stk1.pop())
#         elif l == ">":
#             if len(stk2) > 0:
#                 stk1.append(stk2.pop())
#         elif l == "-":
#             if len(stk1) > 0:
#                 stk1.pop()
#         else:
#             stk1.append(l)
            
#     print(''.join(stk1) + ''.join(reversed(stk2)))



# #1935
# N = int(input())
# s = input()
# arr = [int(input()) for _ in range(N)]
# stk = []
# for ch in s:
#     if ch.isalpha(): #피연산자이면
#         stk.append(arr[ord(ch) - ord('A')])
#         continue

#     b = stk.pop()
#     a = stk.pop()
#     if ch == '+':
#         stk.append(a+b)
#     elif ch == '-':
#         stk.append(a-b)
#     elif ch == '*':
#         stk.append(a*b)
#     elif ch == '/': #나눗셈의 경우 연산 순서 중요하므로 주의할 것!
#         stk.append(a/b)

# print(f"{stk[0]:.2f}")








