# 165.Advance sorted function - Python tutorial 163

friuts = ['grapes', 'apple', 'mango']
# sort
friuts.sort()
print(friuts)
fruits2 = ('grapes', 'apple', 'mango')
# fruits2.sort()   this will givve an err as tuple are immutable so
# they do not give sorting fucntion ability to wotk on them

print(sorted(fruits2))

fruits3 = {'grapes', 'apple', 'mango'}

print(sorted(fruits3))

guitars = [
    {'model' : 'yamaha f310', 'price' : 45000},
    {'model' : 'faith neptune', 'price' : 50000},
    {'model' : 'faith apolo venus', 'price' : 35000},
    {'model' : 'tailor 814ce', 'price' : 450000}
]

print(sorted(guitars , key=lambda dct : dct['price'] , reverse=True))