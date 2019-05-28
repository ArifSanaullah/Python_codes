# 157.Filter Function- Python tutorial 154_real

# filter function

def is_even(a):
    return a%2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

evens = tuple(filter(is_even,numbers))
print(f"this is using function {evens}")

# using lambda

evens = tuple(filter(lambda a:a%2==0,numbers))
print(f"this us using lambda funcion {evens}")


# tuple can be iterated as many times as we want but simply filter function dioes not gives more then one prints
# for i in evens:
#     print(i)
# for i in evens:
#     print(i)

# list comprehnesion

new_evens = [i for i in numbers if i%2==0]
print(f"this is using list comprehension {new_evens}")