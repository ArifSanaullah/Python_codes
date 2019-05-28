# 161.Advance Function Practice 1 - Python tutorial 158

# define a function which takes any numbers of lists and takes the average of thier numbers and print them
# for example lists are [1,2,3],[4,5,6],[7,8,9]
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# try to make such function for two lists and then we will modefy that function for as many lists


# for two list
def avrg_func(l1,l2):
    avrg_list = []
    zip(l1,l2)
    for pair in zip(l1,l2):
        avrg_list.append(sum(pair)/len(pair))
    return avrg_list
print(f"this is for two lists using defined function{avrg_func([1,2,3],[4,5,6])}")


# for as many lists
def avrg_func(*args):
    avrg_list = []
    zip(*args)
    for pair in zip(*args):
        avrg_list.append(sum(pair)/len(pair))
    return avrg_list
print(f"this is for as many lists using defined function{avrg_func([1,2,3],[4,5,6],[7,8,9])}")



# using lambda
avg_lambda = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(f"this is for as many lists using lambda {avg_lambda([1,2,3],[4,5,6],[7,8,9])}")