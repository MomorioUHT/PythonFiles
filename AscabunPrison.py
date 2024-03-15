n = int(input())
num = int(input())

people = [i+1 for i in range(n)]
killed = []

index = 0

for i in range(n):
    while people[index] == 0:
        index += 1
        if index == n: index = 0
    
    count = 1
    
    while (count < num):
        index += 1
        if index == n: index = 0
        if people[index] == 0: continue
        count += 1
        
    killed.append(people[index])
    people[index] = 0
    
print(*exit)