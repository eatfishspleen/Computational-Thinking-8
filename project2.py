
PC_POINTS = 0
CONSOLE_POINTS = 0
EW_MOBILE_POINTS = 0
print (" ")
print (" ")
print ("GAMING QUIZ")
print("              ")
print ("QUESTION 1")
answer1 = input ("Do you like A-power or B-convenience or C-portability :")
if answer1 == "A" or "a" :
    PC_POINTS +=1
elif answer1 == "B" or "b" :
    CONSOLE_POINTS +=1
elif answer1 == "C" or "a" :
    EW_MOBILE_POINTS +=1
print("QUESTION 2")
answer2 = input ("do you prefer A-Skill or B-simplicity C-easy to learn controles :")
if answer1 == "C" or "c" and answer2 == "C" or "c" :
    print ("Sorry we don't like mobile players here so were gatekeeping")
elif answer1 == "A" or "a" or "B" or "b" and answer2 == "A" or "a" or "B" or "b" :
    print ("ok so we both don't like mobile so Ill remove the option")
elif answer2 == "A" or "a":
    PC_POINTS +=1
elif answer2 == "B" or "b" :
    CONSOLE_POINTS +=1
elif answer2 == "C" :
    EW_MOBILE_POINTS +=1
print("QUESTION 3")
answer3 = input ("do you prefer A-custom price or B-set price  :")
if answer3 == "A" :
    PC_POINTS +=1
elif answer3 == "B" or "b":
    CONSOLE_POINTS +=1
print("QUESTION 4")
answer4 = input ("do you prefer A-keyboard and mouse or B-controller  :")
if answer4 == "A" or "a" :
    PC_POINTS +=1
elif answer4 == "B" or "b" :
    CONSOLE_POINTS +=1
print ("QUESTION 5")
answer5 = input ("do you prefer A-customizability or B-uncustomizable :")
if answer5 == "A" or "a" :
    PC_POINTS +=1
elif answer5 == "B" or "b" :
    CONSOLE_POINTS +=1
if PC_POINTS >= CONSOLE_POINTS and PC_POINTS >= EW_MOBILE_POINTS :
    print ("-----------------------------")
    print ("A PC would be best for you")
elif CONSOLE_POINTS >= PC_POINTS and CONSOLE_POINTS >= EW_MOBILE_POINTS :
    print ("--------------------------------")
    print("A console would be best for you")
elif EW_MOBILE_POINTS >= PC_POINTS and EW_MOBILE_POINTS >= CONSOLE_POINTS :
    print ("--------------------------------")
    print ("A mobile device would suit you")