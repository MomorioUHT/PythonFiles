tries = 0
guessed = []
displaying = ''
Answer = str(input())

for i in range(len(Answer)): displaying += '-'

def correct(letterlist, underscore_text, correct_text):
    underscore_text_list = [i for i in underscore_text]
    correct_text_list = [i for i in correct_text]
    
    for i in letterlist:
        for j in range(len(correct_text_list)):
            if correct_text_list[j] == i: underscore_text_list[j] = i      
            
    temp = ''
    for i in underscore_text_list: temp += i
    print(temp)
    
while tries < 6:
    Guess = input()
    if Guess == '0': break
    elif Guess in guessed: continue
    elif Guess not in guessed and Guess not in Answer: tries += 1
    guessed.append(Guess)
    
correct(guessed, displaying, Answer)