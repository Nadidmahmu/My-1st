n = int(input())
free = 0
for i in range(n):
    p, q = map(int, input().split())
    if q - p == 1:
        free += 0
    elif p < q:
        free += 1
    else:
        free += 0
print(free)
