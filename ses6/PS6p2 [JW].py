def battingAverage(hits, atBats):
  average = float(hits)/float(atBats)

  return average

lastName = str(input("ENTER LAST NAME: "))
hits = float(input("ENTER NUMBER OF HITS: "))
atBats = float(input("ENTER NUMBER OF AT BATS: "))

average = battingAverage(hits, atBats)
print()
print("NAME: ",    lastName)
print("AVERAGE: ", average)

