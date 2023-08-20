print("\t\t\t\t**Guess the number**\t\t\t\t ")

import random

main_num=random.randint(100,999)
guess=0
while True:
    ur = int(input("Guess a 3 digit number-->\t"))
    if ur < 0: 
      print("invaliddd")
      exit()
    elif ur < main_num:
      print("Guess higher")
      guess+=1 
    elif ur > main_num:
      print("Guess lower")
      guess+=1
      continue
    elif ur == main_num:
      print("You got it gal")
      break
    else :
      print("Thats not a number I recognize.")

print ("Congratulations!! It only took you ",guess,"attempts to guess the number successfully")
      
    
