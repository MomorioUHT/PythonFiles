context = str(input())
vowels = ' '.join([i for i in context if i.lower() in ["a","e","i","o","u"]])
alpha = ' '.join([i for i in context if i.lower() not in ["a","e","i","o","u"] and i.isalpha()])
number = ' '.join([i for i in context if i.isdigit()])
if vowels != "": 
    print("Vowel(s):")
    print(vowels)
if alpha != "": 
    print("Alphabet(s):")
    print(alpha)
if number != "": 
    print("Number(s):")
    print(number)