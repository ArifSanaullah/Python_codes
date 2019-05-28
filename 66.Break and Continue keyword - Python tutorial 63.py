#66.Break and Continue keyword - Python tutorial 63
#for i in range(1,11):
  #  if i == 11:
 #       break
#    print(i)
#now continue
#if we have to print  1 to 10 but not 5 in the range then we will use continue statment
for i in range(1,11):
    if i == 5:
        continue
    print(i)