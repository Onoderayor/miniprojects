#this is my 4th and my favorate project so far 

name = input("TYPE YOUR NAME! :) ")
print("WELCOME",name,"TO THIS ADVENTURE!")

answer = input(" YOU are on a dirt road, it has come to an end and you can go left and right. which way would you like to go? ").lower()

if answer == "left" :
    answer = input("You come to a river, you can walk arourd it or swim across it? Type walk to walk around and swim to swim across.").lower()

    if answer == "swim":
       print("You swam across and were eaten by aligator.")
         
    elif answer == "walk":
       print("You walked for miles and Died from exaustion.")
       
    else:
       print("Not a valid option. you lose.")


elif answer == "right":
  answer = input("You come to bridge, it looks worn down, do you want to cross it or head back (cross/back) ").lower()

  if answer == "cross":
      answer = input("you cross the bridge and meet a stanger. do you talk to them or ignore them (yes/no) ").lower()

      if answer =="yes":
         print("you talk to the stranger and they give you gold. YOU WIN! ")
         
      elif answer == "no":
         print("you don't talk to the stranger he gets mad. YOU LOSE!")

      else:
       print("Not a valid option. you lose.")
     
  elif answer == "back":
       print("you go back and lose .")
       
  else:
       print("Not a valid option. you lose.")

else:
  print("Not a valid option. you lose.")

print("THANK YOU FOR TRYING",name)
