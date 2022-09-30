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

