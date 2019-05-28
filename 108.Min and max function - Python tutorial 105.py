# 108.Min and max function - Python tutorial 105

numbers = [10,20,30,40,100]
print(min(numbers))
print(max(numbers))
# if we want to check the difference between greatest and smallest number in the list then the
def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(numbers))