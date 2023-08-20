import random

print("🎲🎲INFINITY DICE🎲🎲")

def infi_dice():
  while True:
    play= input("Do you want to roll the dice?")
    u_side=int(input("Enter number of sides that you want your dice to have\n---->\n"))
    if play=="YES" or "yes" or "Yes":
      print("You rolled",random.randint(1,u_side))
    else :
        print("k buddy. Bye then")

infi_dice()

