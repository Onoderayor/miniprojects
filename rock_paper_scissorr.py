# this is my 3rd project


import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
  user_input = input("TYPE ROCK/PAPER/SCISSOR OR Q TO QUIT! :) ").lower()
  if user_input == "q" :
    break

  if user_input not in options:
    continue 

  
  random_number = random.randint(0,2)
  # rock : 0, paper : 1, scissor : 2
  computer_pick = options[random_number]
  print("computer picked", computer_pick + ".")

  if user_input == "rock" and computer_pick == "scissor":
    print("YOU WON! ")
    user_wins += 1
    
  elif user_input == "paper" and computer_pick == "rock":
    print("YOU WON! ")
    user_wins += 1
  

  elif user_input == "scissor" and computer_pick == "paper":
    print("YOU WON! ")
    user_wins += 1

  elif user_input == computer_pick:
    print("you and computer tied!")
    continue
    
  else:
    print("YOU LOST!")
    computer_wins += 1

print("you won",user_wins,"times.")  
print("the computer won",computer_wins,"times.") 
print("GOODBYE! :) ")