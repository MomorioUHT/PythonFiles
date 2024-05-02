NumberOne = str(input()) #+6000000
first1 = str(input()) #+4000
first2 = str(input()) #+4000
ends1 = str(input()) #+4000
ends2 = str(input()) #+4000
TwoSecond = str(input()) #+2000
Yours = str(input())

total = 0
prices = 0
if Yours == NumberOne: 
    total += 6000000
    prices += 1
if Yours.startswith(first1) or Yours.startswith(first2): 
    total += 4000
    prices += 1
if Yours.endswith(ends1) or Yours.endswith(ends2):
    total += 4000
    prices += 1
if Yours.endswith(TwoSecond): 
    total += 2000
    prices += 1

if prices == 0: print("Better luck next time...")
else:
    if prices == 1: print(f"You win {prices} price.")
    else: print(f"You win {prices} prices")
    
    print(f"Total = {total} THB")
    print(f"TAX 7% = {0.07*total:.2f} THB")
    print(f"You got {0.93*total:.2f} THB")