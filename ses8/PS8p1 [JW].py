import time

start = 1
stop = 25
increment = 2
count = start
print("While loop counting ",start," to ",stop," by ",increment,".")

while count <= stop:
  print(count)
  count = count + increment 
  time.sleep(.1)


