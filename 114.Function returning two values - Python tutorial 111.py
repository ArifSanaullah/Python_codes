# 114.Function returning two values - Python tutorial 111
# when wver functions returns two values it returns in the form of tuple if we need seperately then we can do this
def twovals(int1,int2):
    add = int1 + int2
    multiply = int1 * int2
    return add,multiply
add, multiply = twovals(2,5)
print(f"this is tuple {twovals(2,5)}")
print(add)
print(multiply)