# this is my 1st python project ever with the help of youtuber tech with tim

print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
  quit()

print("okay! let's play :)")
score = 0


answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
  print("correct")
  score += 1
else:
  print("incorrect! ")

answer = input("what does gpu stand for? ")
if answer.lower() == "graphical processing unit":
  print("correct")
  score += 1
else:
  print("incorrect! ")

answer = input("what does ram stand for? ")
if answer.lower() == "random acess memory":
  print("correct")
  score += 1
else:
  print("incorrect! ")

answer = input("what does psu stand for? ")
if answer.lower() == "power supply":
  print("correct")
  score += 1
else:
  print("incorrect! ")

print("YOU GOT " + str(score) + " QUESTIONS COREECT! :)") 
print("YOU GOT " + str((score / 4) * 100) + "  % COREECT! :)") 

