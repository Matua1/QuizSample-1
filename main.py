#This is a trivia game about Paul Resnick! Make additions, modifications, and deletions as necessary.
#The code is purposefully buggy. Refer to PS6 with the hangman game to fix this one!
#Ideas for changes: what happens when the user enters something other than true or false, more trivia, different wording, tests
#I will be using the time module to give the user the impression that they are having a conversation with the computer.
import time


typewriter = print
#typewriter effect
def typewriter(string):
  listString = list(string)
  for char in listString:
    print(char, end = "", flush = True)
    time.sleep(0.02)
     
    

typewriter ("Welcome to the Pap High Clean Water Project! You WIN by avoiding 4 WRONG answers.")
wrong_answers = 0
right_answers = 0
while wrong_answers < 4:
    a = input('Paul Resnick met Obama. True or false?')
    if a.upper() == "FALSE":
        wrong_answers += 1
    elif a.upper() == "TRUE":
        right_answers += 1
    b = input('Paul Resnick taught at U-M for 8 years. True or false?')
    if b.upper() == "TRUE":
        wrong_answers += 1
    elif b.upper() == "FALSE":
        right_answers += 1
    c = input('Paul Resnick has a treadmill in his office. True or false?')
    if c.upper == "FALSE":
        wrong_answers += 1
    elif c.upper == "TRUE":
        right_answers += 1
    d = input('Paul Resnick has counted to infinity... twice. True or false?')
    if d.upper == "FALSE":
        wrong_answers += 1
    elif d.upper == "TRUE":
        right_answers += 1
    e = input('Paul Resnick is 6\'3\". True or false?')
    if e.upper == "FALSE":
        wrong_answers += 1
    elif e.upper == "TRUE":
        right_answers += 1 
    f = input("SI 106 is Paul Resnick's favorite section to teach... True or false?")
    if f.upper == "FALSE":
        wrong_answers += 1
    elif f.upper == "TRUE":
        right_answers += 1
    g = input("Paul Resnick is going to give his entire SI 106 section an A... True or false?")
    if g.upper == "FALSE":
        wrong_answers += 1
    elif g.upper == "TRUE":
        right_answers +=1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers < 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        print ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
    h = input("Paul Resnick plays the fiddle. True or false?")
    if g.upper == "FALSE":
        wrong_answers += 1
    elif g.upper == "TRUE":
        right_answers +=1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers < 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        typewriter ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
    break


typewriter(string)