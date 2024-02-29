result = [str(i) for i in str(input()).split(" ")]

def printLadder(number: int, starting: str):
    spaceLen = 9 - (len(result[0]) + len(result[1]))
    if (starting.lower() == "left"):
      print("A       B")
      print("|--------")
      for _ in range(number):
        print("=========")
        print("--------|")
        print("=========")
        print("|--------")
      
    elif (starting.lower() == "right"):
      print("B       A")
      print("--------|")
      for _ in range(number):
        print("=========")
        print("|--------")       
        print("=========")
        print("--------|")
    print(f"{result[0]}{' '*spaceLen}{result[1]}")

    print("Game End")
    if (float(result[1]) > float(result[0])):
      if starting.lower() == "right":
        print(f"A is the Winner, got {result[1]}")
        print(f"B is the Loser, got {result[0]}")
      else:
         print(f"B is the Winner, got {result[1]}")
         print(f"A is the Loser, got {result[0]}")       
    if (float(result[0]) > float(result[1])):
      if starting.lower() == "right":
         print(f"B is the Winner, got {result[0]}")
         print(f"A is the Loser, got {result[1]}") 
      else:
         print(f"A is the Winner, got {result[0]}")
         print(f"B is the Loser, got {result[1]}") 

starting = str(input())
amount = int(input())
printLadder(amount,starting)