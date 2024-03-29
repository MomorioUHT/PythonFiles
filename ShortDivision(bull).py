initial = str(input())
divisor = str(input())

allLen = len(divisor) + len(initial) + 3
frontlen = len(divisor)
backlen = allLen - frontlen
spaces_needed = backlen - len(str(result)) - 1

result = int(initial)//int(divisor)

print(f"{divisor} | {initial}")
print(" "*frontlen,"-"*backlen)
print(" "*(frontlen + spaces_needed), result)
print(" "*frontlen,"-"*backlen)

if (int(initial)%int(divisor) != 0):
    print(f"Remainder is {int(initial)%int(divisor)}")