n = int(input())
p = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    receiver = p[i] - 1
    giver = i + 1
    result[receiver] = giver
print(" ".join(map(str, result)))

