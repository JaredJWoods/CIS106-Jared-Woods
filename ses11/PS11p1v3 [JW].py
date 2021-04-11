#---------------------------------MODULE_IMPORT-------------------------------------
import time #time is for my delay between lines
import sys  #sys is beyond me but something I needed for the "typing" effect


#----------------------------------VARIABLES-----------------------------------------
index = int(input("#1 Enter how many assignments you have completed:  "))
scores = [None] * index
scores2 = [500, 600, 700, 800, 900]
grades = ["A", "B", "C", "A", "A", "C"]
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
mdel = 1.2 #this is a medium time delay used in between items to make it readable
sdel = .03 #this is a short delay used for 'typing' char effect



#---------------------------------FUNCTIONS-------------------------------------------
def printScores(scores):
    print()
    for score in range(0, len(scores)):
        print("\t\tSCORE " + format(str(score + 1), '>2') + ": " +
              str(scores[score]) + "\t\t ")
        time.sleep(.04)
    time.sleep(mdel)
    print()
#recurring score printing function

def userInput(scores):
    print()
    for char in "Now you must enter " + str(index) + " assignment scores.":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    print()
    for score in range(0, len(scores)):
        scores[score] = int(input("\t\tEnter Score " + str(score + 1) + ": "))
    print()
    for char in "Well Done! Here is what you entered:":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel)
#User input and display of scores

def lateEntry(scores):
    for char in "#2 Whoops! Almost forgot one...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    print()
    scores.insert(0, 99)
    time.sleep(mdel)
    for char in "... I will add it at the top.":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel)
#2 insert function

def scoreChange(scores):
    for char in "#3 Let me help that first score out a bit...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    scores[0] = 100
    time.sleep(mdel)
#3 item change 99-100

def scoresExt(scores):
    for char in "#4 I found scores from earlier":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    print()
    time.sleep(mdel)
    for score in range(0, len(scores2)):
        print("\t\tSCORE  " + str(score + 1) + ": " + str(scores2[score]) +
              "\t\t ")
        time.sleep(.04)
    print()
    time.sleep(mdel)
    for char in "Let me combine these scores with the ones you entered...":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    scores.extend(scores2)
    time.sleep(mdel)
#4 list extension

def scoreRemove(scores):
    for char in "#5 I added a score of 800 by mistake...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel)
    print()
    for char in "...let me remove it":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    scores.remove(int(800))
    time.sleep(mdel)
#5 Item removal via search

def scorePop(scores):
    for char in "#6 The third score " + str(scores[2]) + " is invalid.":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel)
    for char in "...I will remove that.":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    scores.pop(2)
    time.sleep(mdel)
#6 Item removal via index

def gradeList(grades):
    look_for = "F"
    for char in "---------------------------------------------------------------\n":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    for char in "# 7 That is it for scores now let us look at the letter grades\n":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    A_grades = grades.count("A")
    for char in "# 8 There are " + str(A_grades) + " A grades in the list\n":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    B_index = grades.index("B")
    for char in "# 9 The first B is in index: " + str(B_index) + "\n":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    if look_for in grades:
        print("#10 " + str(look_for) + " is at index " +
              str(grades.index(look_for)) + "\n")
    else:
        print("#10 There are no " + str(look_for) + "'s in the grade list")
    for char in "---------------------------------------------------------------":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel * 2)
    print()
#7-10 grades exercises

def clearScores(scores2):
    scores2.clear()
    print("\n#11 Scores2 list cleared " + str(scores2))
#11 clear function

def delScores(scores2):
    del scores2
    print("#12 scores2 has been deleted: the following error is intentional")
    print(scores2)
    time.sleep(mdel)
#12 delete function

def playerList(players):
    print("\n**************************************************************")
    print("#13 Initial List:  " + str(players))
    players.sort()
    time.sleep(mdel)
    print("#14 Sorted List:   " + str(players))
    players2 = players.copy()
    time.sleep(mdel)
    print("#15 Copied List:   " + str(players2))
    players2.reverse()
    time.sleep(mdel)
    print("#16 Reversed List: " + str(players2))
    print("**************************************************************\n")
#13-16 various sorting and copying functions

def intro():
    for char in "WEEK 11 - Jared Woods\n":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(sdel)
    time.sleep(mdel)
#Intro test to see if I could get one character to print on a line




#---------------------------------CODE_EXECUTION----------------------------------
#runs all functions in a neat order
userInput(scores)
printScores(scores)
lateEntry(scores)
printScores(scores)
scoreChange(scores)
printScores(scores)
scoresExt(scores)
printScores(scores)
scoreRemove(scores)
printScores(scores)
scorePop(scores)
printScores(scores)
gradeList(grades)
playerList(players)
intro()
#the follwing were moved to the end due to the error causing the program to stop
clearScores(scores2)
delScores(scores2)
#------------------------------------END-----------------------------------------