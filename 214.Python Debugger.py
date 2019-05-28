# 214.Python Debugger

import pdb
# according to wiipedia "debugging is the process of finding and fixing the error in your code"

# why debugging
# 1.) our programe is not working
# 2.) our programe is working but not the way we want.


# steps for debugging
# 1.) set trace
# 2.) execute code line by line

pdb.set_trace() # this line can be written in any code block
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"hello {name} your age is {age}")
print(f"you will  be {age+5} in next five years")