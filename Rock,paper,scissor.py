from getpass import getpass as input
print("🧩ROCK PAPER SCISSOR🧩\n\nPick your moves players\n(R/P/S)")
p1= input("Player 1-->\t")
p2= input("Player 2-->\t")

if (p1==("R") and p2==("R") ) or (p1==("P")) and (p2==("P")) or (p1==("S") and (p2==("S"))) :
  print("It's a tie")
elif (p1==("R") and p2==("S") ) :
  print("p1 has absolutely destroyed p2 with the rock\n*** WINNER IS:PLAYER1 ***\n 🪨🗞✂️*****🪨🗞✂️")
elif (p1==("S") and p2==("R") ) :
  print("p2 has absolutely destroyed p1 with the rock\n*** WINNER IS:PLAYER2 ***\n  🪨🗞✂️*****🪨🗞✂️")
elif (p1==("P") and p2==("R")):
  print("p1 paper is unfazed by p2's rock\n*** WINNER IS:PLAYER1 ***\n  🪨🗞✂️*****🪨🗞✂️")
elif (p1==("R") and p2==("P")):
  print("p2 paper is unfazed by p1's rock\n*** WINNER IS:PLAYER2 ***\n  🪨🗞✂️*****🪨🗞✂️")
elif (p1==("P") and p2==("S")):
  print("p1 has cut p2 up into pieces\n*** WINNER IS:PLAYER1 ***\n  🪨🗞✂️*****🪨🗞✂️")
elif (p1==("S") and p2==("P")):
  print("p2 has cut p1 up into pieces\n*** WINNER IS:PLAYER2 ***\n  🪨🗞✂️*****🪨🗞✂️")
  
