# 163.any and all practice - Python tutorial 161

def my_sum (*args):
    # args = ()
    if all([type(arg) == int or type(arg) == complex or type(arg) == float for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong Input"
print(my_sum(1,2,4,3,1+9j))