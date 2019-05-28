# 50.If-elif-else statement - Python tutorial 47
# if elif else statement
# ticket pricing according to age
# if age is 1 to 3 then ticekt rate is free of cost
# 4 to 10 then 150 rupees
# 11 to 60 then 250
# more then 60 then 200
# or any other value like negative value or zero will print you can not watch the movie
age = int(input('please input your age : '))
if age == 0 or age < 0:
    print('Sorry....! You can not watch the movie.')
elif 0 < age <= 3:
    print('ticket rate for you is rupee 150 only.')
elif 4 <= age <= 10:
    print('ticket rate for you is rupee 200 only.')
elif 11 <= age <= 60:
    print('ticket rate for you is rupee 250 only.')
else:
    print('ticket rate for you is rupee 200 only.')
