# 162.any and all function - Python tutorial 160

num1 = [1,2,3,4,5,6,7,8]
num2 = [2,4,6,8]

# without all and any function
evens = []
for even in num1:
        evens.append(even%2==0)
print(f"this is simple for loop coding {evens}")

true1 = any([False, True, False, True, False, True, False, True])
print(f"this is any function {true1}")

true2 = all([False, True, False, True, False, True, False, True])
print(f"this is all function {true2}")

print(f"this is list comprehension for all {all(num%2==0 for num in num1)}")
print(f"this is list comprehension for all {all(num%2==0 for num in num2)}")
print(f"this is list comprehension for any {any(num%2==0 for num in num1)}")
print(f"this is list comprehension for any {any(num%2==0 for num in num2)}")