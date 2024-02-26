amount,data = int(input()),[]
for i in range(0,amount): data.append(int(input()))
money = int(input())
for i in sorted(data)[::-1]:
    print(f"{i}: {money//i}")
    money = money - (money//i)*i