print("****Loan Calculator*****")


initial=int(input("What is loan amount"))
ate=int(input("Rate interest:"))
for i in range(20): 
     initial+=initial*(ate/100) 
     print ("Loan to be paid",initial)
    
