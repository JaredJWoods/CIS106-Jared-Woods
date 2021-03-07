def bowlCalc():
  global averageScore
  global adjustedScore
  averageScore = (game1 + game2 + game3)/3
  adjustedScore = (200-averageScore) * .9
  adjustedScore = adjustedScore + averageScore

print            ("---------BOWLING HANDICAP CALCULATOR-----------")
print()

name =  str(input("Welcome, please enter bowler's name:     "))
print()

game1 = int(input(" Enter the score of your first game:     "))  
game2 = int(input(" Enter the score of your second game:    "))  
game3 = int(input(" Enter the score of your third game:     ")) 
print()

print            ("  -The league basis score is:            200")
print            ("  -The league percentage factor is:      90%")
print() 

bowlCalc()
print            ("Bowler's Name:                          ", name)
print            ("Your average Score                      ", int(averageScore))
print            ("Your adjusted Score                     ", int(adjustedScore))
print()
print            ("----------------------------------------------")