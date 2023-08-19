print("*$*$*List Generator*$*$*")
star_val=int(input("Start at:\t"))
end_val=int(input("End prior to:\t"))
inc=int(input("Increament b/w values:\t"))

for i in range(star_val,end_val,inc):
  print (i,"Days")

