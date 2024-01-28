data = []

def find_mode(l):
    result = []
    mode = list(range(11))
    for i in range(len(mode)):
        count = 0
        for j in l:
            if j == i:
                count += 1
        mode[i] = count
    
    for i in range(len(mode)):
        if mode[i] == max(mode):
            result.append(i)
            
    for i in result:
        print(i)

i = 0  
while i < 20 :
    x = int(input("Enter score: "))
    if (x >=0 and x <= 10):
        data.append(x)
        i += 1
    else :
        print("Score is out of range.")

print("-----")
print("Original list:")
print(data)
print("Mode of scores:")      
find_mode(data)