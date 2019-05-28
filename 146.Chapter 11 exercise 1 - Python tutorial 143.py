# 146.Chapter 11 exercise 1 - Python tutorial 143

def args_to_the_power_num(num , *args):
    if args:
        print(f"your entered list is: {args}")
        print(f"the number you entered4 is: {num}")
        return [i**num for i in args]
    else:
        return "you didn't entered any list"
        # print(to_power)
        # return to_power


a = [ 1 , 2 , 3 , 4 ]
print(args_to_the_power_num(2,*a))
