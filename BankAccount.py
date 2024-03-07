balance = 0
while True:
    x = str(input()).split(" ")
    if x[0] == 'exit': break
    if x[0] == 'deposit': balance += float(x[1])
    if x[0] == 'withdraw': 
        if float(x[1]) > balance: break
        else: balance -= float(x[1])
    if balance < 0: break
print(f"balance = {balance:.2f}")