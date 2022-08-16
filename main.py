#This is a trivia game about Pollution in our waterways.
#Matua Halafihi
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
time.sleep(1)
wrong_answers = 0
right_answers = 0
score = right_answers + wrong_answers


while wrong_answers < 4:
    typewriter('\nMany people on EARTH do not have access to clean water. True or false? ')
    a=input()
    if a.upper() == "FALSE":
        wrong_answers -= 1
        print("\nIncorrect. Your score is", score)
    elif a.upper() == "TRUE":
        right_answers += 1
        score = +1
        typewriter('''         , ;MMMM..
                    ,;:MM"MMMMM.
                ,;.MM::M.MMMMMM:
              ""::.;'MMMMMMMMM
                    "'""MMMMM;
                      ':MMMM.
                      'MMMM;
                      :MMMM;.
                      MMMMMM;...
                     MMMMMMMMMMMMM;.;..
                    MMMMMMMMMMMMMMMMMMM...
                   MMMMMM:MMMMMMMMMMMMMMM;...       ..:
                  MMMMMM;MMMMMMMMMMMMM:MMMMMMM:MMMM:M
                 :MMMMMM:MMMMMMMMMMMMMMM.:::;:::;;:'
               ':MMMMMMM:MMMM:;MM:M;.MMM:';::M:'
                ':MMMMMM;M;;MM;::M;;::::;MM:""
                  'MMMMMMMM;M;:::MMMMMMMMMM"
                   ''MMMMMMMMMMMMMMMMMMMMM"
                      ':MMMMMMMMMMMMMMMM"'
                        '':MMMMMMMMMMM"'
                           ':MMMMMM""'
                              .
                              :
                              ::
                          ,..;.M'
                         ,;;MM:'
                         ''')
        time.sleep(0.4)
        print("Correct!, your score is", score)
    typewriter('\nPhysical water pollution includes waste being thrown on the ground. TRUE or FALSE ? ')
    b = input()
    if b.upper() == "FALSE":
        wrong_answers -= 1
        print("\nIncorrect, your score is", score)
    elif b.upper() == "TRUE":
        right_answers += 1
        score += 1
        typewriter('''                                 .....
                            .e$$$$$$$$$$$$$$e.
                          z$$ ^$$$$$$$$$$$$$$$$$.
                        .$$$* J$$$$$$$$$$$$$$$$$$$e
                       .$"  .$$$$$$$$$$$$$$$$$$$$$$*-
                      .$  $$$$$$$$$$$$$$$$***$$  .ee"
         z**$$        $$r ^**$$$$$$$$$*" .e$$$$$$*"
        " -\e$$      4$$$$.         .ze$$$""""
       4 z$$$$$      $$$$$$$$$$$$$$$$$$$$"
       $$$$$$$$     .$$$$$$$$$$$**$$$$*"
     z$$"    $$     $$$$P*""     J$*$$c
    $$"      $$F   .$$$          $$ ^$$
   $$        *$$c.z$$$          $$   $$
  $P          $$$$$$$          4$F   4$
 dP            *$$$"           $$    '$r
.$                            J$"     $"
$                             $P     4$
F                            $$      4$
                            4$%      4$
                            $$       4$
                           d$"       $$
                           $P        $$
                          $$         $$
                         4$%         $$
                         $$          $$
                        d$           $$
                        $F           "3
                 r=4e="  ...  ..rf   .  ""% Gilo94'
                $**$*"^""=..^4*=4=^""  ^""" ''')
        print("Correct!, your score is", score)
    typewriter('\nWhat causes more damage to our rivers and streams? A) Oil\nB) Grass Clippings ')
    c = input()
    if c.upper() != "A":
        
        print("\nIncorrect, your score is", score)
        wrong_answers -= 1
    elif c.upper() == "A":
        right_answers += 1
        score += 1
        typewriter('''                                 .....
                            .e$$$$$$$$$$$$$$e.
                          z$$ ^$$$$$$$$$$$$$$$$$.
                        .$$$* J$$$$$$$$$$$$$$$$$$$e
                       .$"  .$$$$$$$$$$$$$$$$$$$$$$*-
                      .$  $$$$$$$$$$$$$$$$***$$  .ee"
         z**$$        $$r ^**$$$$$$$$$*" .e$$$$$$*"
        " -\e$$      4$$$$.         .ze$$$""""
       4 z$$$$$      $$$$$$$$$$$$$$$$$$$$"
       $$$$$$$$     .$$$$$$$$$$$**$$$$*"
     z$$"    $$     $$$$P*""     J$*$$c
    $$"      $$F   .$$$          $$ ^$$
   $$        *$$c.z$$$          $$   $$
  $P          $$$$$$$          4$F   4$
 dP            *$$$"           $$    '$r
.$                            J$"     $"
$                             $P     4$
F                            $$      4$
                            4$%      4$
                            $$       4$
                           d$"       $$
                           $P        $$
                          $$         $$
                         4$%         $$
                         $$          $$
                        d$           $$
                        $F           "3
                 r=4e="  ...  ..rf   .  ""% Gilo94'
                $**$*"^""=..^4*=4=^""  ^""" ''')
        print("Correct!, your score is", score)
    typewriter('A significant ocean pollution is\nA) Rubbish\nB) Plastic\nC) Toxic waste? ')
    d = input()
    if d.upper() != "b":
        wrong_answers -= 1
        print("\nIncorrect, your score is ", score)
    elif d.upper() == "b":
        right_answers += 1
        score += 1
        typewriter('''                                 .....
                            .e$$$$$$$$$$$$$$e.
                          z$$ ^$$$$$$$$$$$$$$$$$.
                        .$$$* J$$$$$$$$$$$$$$$$$$$e
                       .$"  .$$$$$$$$$$$$$$$$$$$$$$*-
                      .$  $$$$$$$$$$$$$$$$***$$  .ee"
         z**$$        $$r ^**$$$$$$$$$*" .e$$$$$$*"
        " -\e$$      4$$$$.         .ze$$$""""
       4 z$$$$$      $$$$$$$$$$$$$$$$$$$$"
       $$$$$$$$     .$$$$$$$$$$$**$$$$*"
     z$$"    $$     $$$$P*""     J$*$$c
    $$"      $$F   .$$$          $$ ^$$
   $$        *$$c.z$$$          $$   $$
  $P          $$$$$$$          4$F   4$
 dP            *$$$"           $$    '$r
.$                            J$"     $"
$                             $P     4$
F                            $$      4$
                            4$%      4$
                            $$       4$
                           d$"       $$
                           $P        $$
                          $$         $$
                         4$%         $$
                         $$          $$
                        d$           $$
                        $F           "3
                 r=4e="  ...  ..rf   .  ""% Gilo94'
                $**$*"^""=..^4*=4=^""  ^""" ''')
        print("\nCorrect!, your score is ", score)
    typewriter('\nFluoride is added to our water supply to help strenghten teeth and fight cavities? TRUE or FALSE  ')
    e = input()
    if e.upper() == "FALSE":
        wrong_answers -= 1
        print("\nIncorrect, your score is ", score)
    elif e.upper() == "TRUE":
        right_answers += 1 
        score += 1
        typewriter('''            , ;MMMM..
                    ,;:MM"MMMMM.
                ,;.MM::M.MMMMMM:
              ""::.;'MMMMMMMMM
                    "'""MMMMM;
                      ':MMMM.
                      'MMMM;
                      :MMMM;.
                      MMMMMM;...
                     MMMMMMMMMMMMM;.;..
                    MMMMMMMMMMMMMMMMMMM...
                   MMMMMM:MMMMMMMMMMMMMMM;...       ..:
                  MMMMMM;MMMMMMMMMMMMM:MMMMMMM:MMMM:M
                 :MMMMMM:MMMMMMMMMMMMMMM.:::;:::;;:'
               ':MMMMMMM:MMMM:;MM:M;.MMM:';::M:'
                ':MMMMMM;M;;MM;::M;;::::;MM:""
                  'MMMMMMMM;M;:::MMMMMMMMMM"
                   ''MMMMMMMMMMMMMMMMMMMMM"
                      ':MMMMMMMMMMMMMMMM"'
                        '':MMMMMMMMMMM"'
                           ':MMMMMM""'
                              .
                              :
                              ::
                          ,..;.M'
                         ,;;MM:'
                         ''')
    print("\nCorrect, your score is ", score)
    typewriter("\nHow much of the water on Earth is available as fresh water for drinking?\nA) 100%\nB) 50%\nC) 25%\nD) 1%  ")
    f = input()
    if f.upper() != "d":
      wrong_answers -= 1
      print("\nIncorrect, your score is ", score)
    elif f.upper() == "d":
       right_answers += 1
       score += 1
    typewriter("\n5000 children die each because of dirty water. True or false?")
    g = input()
    if g.upper() == "FALSE":
        wrong_answers += 1
        print("\nIncorrect, your score is ", score)
    elif g.upper == "TRUE":
        right_answers +=1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers < 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        print ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
        typewriter("\nWhat happens to plastic waste when left in the environment? \nA) It is a biodegradable material so it eventually disintegrates\nB) It never fully goes away, it just breaks into little pieces\nC) There is no such thing as plastic waste, all plastic is recycled.")
    h = input()
    if h.upper() != "b":
        wrong_answers -= 1
        typewriter("Incorrect")
    elif h.upper() == "b":
        right_answers +=1
        score += 1
    if wrong_answers >= 4:
        print ('You lose!')
    if wrong_answers <= 4:
        typewriter ('Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!')
        typewriter ('You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.')
    break

typewriter(string)