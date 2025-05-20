import random
import time
print ("-Time-Boom-")
count = 0

random_value = random.randint(1, 2)

while True:

  if count == 0:
    print("◻◻◻◻◻◻◻◻◻◻")
  if count == 1:
    print("◻◼◻◻◻◻◻◻◻◻")
  if count == 2:
    print("◼◼◻◻◻◻◻◻◻◻")
  if count == 3:
    print("◼◼◼◻◻◻◻◻◻◻")
  if count == 4:
    print("◼◼◼◼◻◻◻◻◻◻")
  if count == 5:
    print("◼◼◼◼◼◻◻◻◻◻")
  if count == 6:
    print("◼◼◼◼◼◼◻◻◻◻")
  if count == 7:
    print("◼◼◼◼◼◼◼◻◻◻")
  if count == 8:
    print("◼◼◼◼◼◼◼◼◻◻")
  if count == 9:
    print("◼◼◼◼◼◼◼◼◼◻")
  if count == 10:
    print("◼◼◼◼◼◼◼◼◼◼")

choice = input("- ")
if choice == "1":
  print("You played 1")
  count +=1
  if count >= 10:
    print("Boom!")
    print("You lose!")
    print(f"The count ended at {count}")
    break
  else:
    time.sleep(1)
    count += random_value
    print(f"Computer played {random_value}")
    time.sleep(0.3)
    print(f"The count is {count}")
elif choice == "2":
  print("You played 2")
  count +=2

  if count >= 10:
    print("Boom!")
    print("You lose!")
    print(f"The count ended at {count}")
  else:
    time.sleep(1)
    count += random_value
    print(f"Computer played {random_value}")
    time.sleep(0.3)
    print(f"The count is {count}")
else: 
  print("Invalid input")
if count >= 10:
  print("Boom!")
  print("You win!")
  print(f"The count ended at {count}")
  break



  



