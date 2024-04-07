import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for i in range(n):
    s[i] -= b
    
    if s[i] > 0:
        result += (s[i] // c)
        s[i] = s[i] % c
        
        if s[i] > 0:
            result += 1

print(result)
