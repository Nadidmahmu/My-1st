n = int(input())

groups = 0
prev_magnet = ""

for i in range(n):
    current_magnet = input()
    
    if i == 0:
        groups = 1
    elif current_magnet != prev_magnet:
        groups += 1
    
    prev_magnet = current_magnet

print(groups)

