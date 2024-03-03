n = int(input())
space = n-1
stars = 1
for i in range(1,n+1):
    print(f"{' '*space}{'*'*stars}")
    print(f"{'*'*stars}{' '*space}")
    space -= 1
    stars += 1