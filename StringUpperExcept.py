text = input().split(" ")
words = ['for','and','with','of']
final = ''
for i in text:
    if len(i) > 0:
        if i.lower() in words: temp = i[0].lower() + i[1::].lower()
        else: temp = i[0].upper() + i[1::].lower()
        final += temp + " "
    else: final += ' '
print(final)