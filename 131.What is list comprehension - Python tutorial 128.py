# 131.What is list comprehension - Python tutorial 128
# converting our lengthy code into samller or smallest

# normal method
sq = []
for i in range(1,11):
    sq.append(i**2)
print(sq)


#list comprehension
sqs = [i**2 for i in range(1,11)]
print(sqs)

# for priniting negative numbers list compensation
negative_numbers = [-i for i in range(1,11)]
print(negative_numbers)

names = ['arif','sanaullah','danish']
first_letter = [name[0] for name in names]
print(first_letter)