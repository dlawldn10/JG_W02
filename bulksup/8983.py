import sys


number_shoot, number_animal, range_shoot = map(int, sys.stdin.readline().split())
shoot_group = list(map(int, sys.stdin.readline().split()))
shoot_group.sort()

animal_group = []
for i in range(number_animal):
    x, y = map(int, sys.stdin.readline().split())
    animal_group.append([x, y])

count = 0

for each_animal in animal_group:
    start = 0
    end = number_shoot-1
    while start <= end:
            mid = (start+end)//2
            distance = abs(each_animal[0] - shoot_group[mid]) + each_animal[1]
            if distance > range_shoot:
                if each_animal[0] < shoot_group[mid]:
                    end = mid - 1
                elif each_animal[0] > shoot_group[mid]:
                    start = mid+1
                else:
                    break
            else:
                count += 1
                break
print(count)
