import time

start =     int(input("Enter starting number:         "))
increment = int(input("Enter skip counting increment: "))
stop =      int(input("Enter stopping number:         "))
print()
count = start
print("       Counting ",start," to ",stop," by ",increment)

while count <= stop:
  print(count)
  count = count + increment 
  time.sleep(.1)

