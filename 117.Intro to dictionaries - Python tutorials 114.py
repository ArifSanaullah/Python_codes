# 117.Intro to dictionaries - Python tutorials 114
#used to store data in random way and can be accessed rendomly
# vast then lists or arrays
# can be stored any type of data even dict in a dict can be stored
#declaration:
user = dict(
    name = 'arif',
    age = 24,
    surname = 'sanaullah',
    cgpa = 3.6,
    fav_mavies = [],
    fav_tunes = []
)
print(user)
print(type(user))
print(user['name'])
print(user['surname'])
print(user['cgpa'])
print(user['fav_mavies'])
users = {
        user: {
            'name' : 'arif' ,
            'age' : 24 ,
            'surname' : 'sanaullah' ,
            'cgpa' : 3.6 ,
            'fav_mavies' : [ ] ,
            'fav_tunes' : [ ],
}
}