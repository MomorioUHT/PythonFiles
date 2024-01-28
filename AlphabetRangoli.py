n = int(input())

def print_rangoli(n):
    import string
    alpha = string.ascii_lowercase
    l=[]
    for i in range(n):
        s = '-'.join(alpha[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    b=reversed(l[1:])
    print("\n".join(b), "\n".join(l), sep = "\n")
    
if n == 1: print("a")
elif n > 26 or n <= 0: print("ERROR")
else: print_rangoli(n)
