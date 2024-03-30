initial,divisor = int(input()),int(input())
allLen = len(str(divisor)) + len(str(initial)) + 3
frontlen = len(str(divisor))
backlen = allLen - frontlen

result = initial//divisor

print(f"{result:>{allLen}}")
print(f"{' '*frontlen} {'-'*backlen}")
print(f"{divisor} | {initial}")

def long_division(initial, divisor, frontlen):
    quotient = ''
    remainder = 0
    initial_str = str(initial)
    
    front_space = frontlen + 3
    
    count = 0
    for i in range(len(initial_str)):
        digit = int(initial_str[i])
        remainder = remainder * 10 + digit
        quotient_digit = remainder // divisor
        product = quotient_digit * divisor
        remainder -= product
            
        if product != 0:
            if count == 0: 
                if (len(str(remainder + product)) > len(str(product))): 
                    front_space += (len(str(remainder + product)) - len(str(product)))
                print(f"{' '*front_space}{product} -")
            else: 
                print(f"{' '*front_space}{remainder + product}")
                if (len(str(remainder + product)) > len(str(product))): 
                    front_space += (len(str(remainder + product)) - len(str(product)))
                print(f"{' '*front_space}{product} -")
            count += 1
            
            print(f"{' '*(front_space)}{'-'*len(str(product))}")
                 
            if (len(str(remainder)) < len(str(product))): front_space += 1
            if (remainder == 0 and i != len(initial_str)-1): front_space += 1
        
        quotient += str(quotient_digit)
        
    print(f"{' '*front_space}{remainder}")    
    print(f"{' '*front_space}{'='*(len(str(remainder)))}")       
    
long_division(initial, divisor, frontlen)