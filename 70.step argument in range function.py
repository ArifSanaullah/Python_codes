#71.For loop and string - Python tutorial 68
#uncomment all this code blocks one by one and see the output


#old way is this
#name ="arif khan"
#for i in range(len(name)):
#    print(name[i])



#this is new way
#name = "arif khan"
#for i in name:
#    print(i)



#12345 -----> 1+2+3+4+5
num = input("enter a number: ")
total = 0
for i in num:
    total += int(i)
print(total)