deck = str(input()).split(" ")

suit_rank = ["C","D","H","S"]
value_rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def helper(card: str): 
    return suit_rank.index(card[-1]),value_rank.index(card[:-1])

print(*sorted(deck, key=helper))