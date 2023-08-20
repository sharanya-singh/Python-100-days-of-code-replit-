print("\t\t\t\tMultiplication table generator\t\t\t\t")

print("Answer the following math questions to test your math skills-->\n")

num=int(input("What table would you like to be tested for?\n"))

counter=0
for i in range(1,num):
  canswer=i*num
  print(i,"x",num)
  answer=int(input("--->"))
  if answer==canswer:
    print("Got that one right")
    counter+=1
  else:
    print("INCORRECT!!The correct ansswer was",canswer)

if counter == 10:
  print("Wow! A perfect score!\n***MATHWIZ***")

else:
  print("You got",counter,"out of 10 correct.")
