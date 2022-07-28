#This is a trivia game about Pollution in our waterways.

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
    typewriter('\nMany people on EARTH do not have access to clean water. True or false? ')
    a=input()
    if a.upper() == "FALSE":
        wrong_answers += 1
    elif a.upper() == "TRUE":
        right_answers += 1
        typewriter(' Physical water pollution includes waste being thrown on the ground. TRUE or FALSE ? ')
        b = input()
    if b.upper() == "TRUE":
        wrong_answers += 1
    elif b.upper() == "FALSE":
        right_answers += 1
        typewriter('Paul Resnick has a treadmill in his office. True or false?')
        c = input()
    if c.upper == "FALSE":
        wrong_answers += 1
    elif c.upper == "TRUE":
        right_answers += 1
        typewriter('Paul Resnick has counted to infinity... twice. True or false?')
    d = input()
    if d.upper == "FALSE":
        wrong_answers += 1
    elif d.upper == "TRUE":
        right_answers += 1
        typewriter('Paul Resnick is 6\'3\". True or false?')
        e = input()
    if e.upper == "FALSE":
        wrong_answers += 1
    elif e.upper == "TRUE":
        right_answers += 1 
        typewriter("SI 106 is Paul Resnick's favorite section to teach... True or false?")
        f = input()
    if f.upper == "FALSE":
        wrong_answers += 1
    elif f.upper == "TRUE":
        right_answers += 1
        typewriter("Paul Resnick is going to give his entire SI 106 section an A... True or false?")
        g = input()
    if g.upper == "FALSE":
        wrong_answers += 1
    elif g.upper == "TRUE":
        right_answers +=1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers < 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        print ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
        typewriter("Paul Resnick plays the fiddle. True or false?")
        h = input()
    if g.upper == "FALSE":
        wrong_answers += 1
    elif g.upper == "TRUE":
        right_answers +=1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers <= 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        typewriter ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
    break


typewriter(string)