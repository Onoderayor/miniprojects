# this is my 2nd project

import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print("plese type a number greater than 0 next time. :)")
    quit()
else:   
   print("plese type a number next time. :)")
   quit()

random_number = random.randint(1,top_of_range)
guesses = 0

while True:
  guesses += 1
  user_guess = input("make a guess :)")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:   
   print("plese type a number next time. :)")
   continue

  if user_guess == random_number:
    print("YOU GOT IT :) ")
    break
  elif user_guess > random_number:
   print("you were above the number !")
  else:
   print("you were below the number !")


print(" YOU got it in ", guesses, "guesses :)")
