deck = str(input()).split(' ')
bot_hand,total_score = [],0

for i in deck:
    if total_score <= 16 and len(bot_hand) <= 5: 
        if i == "J" or i == "Q" or i == "K":  total_score += 10
        elif i == "A":  total_score += 1
        else: total_score += int(i)
        bot_hand.append(i) 

piority = ['K','Q','J','10','9','8','7','6','5','4','3','2','A']
print(sorted(bot_hand, key=lambda x: piority.index(x))[0])
if total_score > 21: print('busted')
else: print(total_score)