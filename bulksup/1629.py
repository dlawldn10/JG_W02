import sys
input = sys.stdin.readline()

input_a, input_b, input_c = map(int, input.split())

def find_remain(a, b, c):
    if b==1:
        return a%c
    else:
        if b%2 == 0:
            b = b//2
            return (find_remain(a,b,c)**2)%c 
        else:
            b = b//2
            return (find_remain(a,b,c)**2 * find_remain(a,1,c))%c

print(find_remain(input_a, input_b, input_c))
