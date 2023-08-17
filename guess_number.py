print("\t\t\t\t**Guess the number**\t\t\t\t ")

guess = 0
pick=230
while True:
    ur = int(input("Guess a 3 digit number"))
    if ur < 0: 
      print("invaliddd")
      exit()
    if ur < pick :
      print("Guess higher")
      guess+=1 
    if ur > pick :
      print("Guess lower")
      guess+=1
      continue
    elif ur == pick :
      print("You got it gal")
      break
    else :
      print("Thats not a number I recognize.")

print ("Congratulations!! It only took you ",guess,"attempts to guess the number successfully")
      


        
    
