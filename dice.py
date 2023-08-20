import random

print("🎲🎲INFINITY DICE🎲🎲")

def infi_dice():
   if play=="yes":
         u_side=int(input("Enter number of sides that you want your dice to have\n---->\n"))
         print("You rolled",random.randint(1,u_side))
   elif play=="no":
         print("k buddy. Bye then")
play= input("Do you want to roll the dice?\n")
infi_dice()
play=input("Do you want to roll again?\n")
infi_dice()
