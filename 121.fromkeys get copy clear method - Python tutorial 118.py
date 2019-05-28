# 121.fromkeys get copy clear method - Python tutorial 118
user_info = dict(
    name = 'arif',
    age = 24,
    surname = 'sanaullah',
    cgpa = 3.6,
    state = 'punjab' ,
    hobbies=[ "coding" , "movies watchng" ],
    fav_movies = ["prince of percia","captain jack sparrow"],
    fav_tunes = ["fairy tales","rising sun"]
)
# fromkeys method is used to create a dict
d = dict.fromkeys(['name', "age", "class"], "unknown")
#print(d)
a = dict.fromkeys(['name', "age", "class"], ["unknown", "unknown"])
#print(a)
b = dict.fromkeys(range(10),"unknown")
#print(b)


#get method
# use get method to acess items of dict bcoz it returns none if key is not found in  the dict
print(user_info.get("name"))
print(user_info.get("names"))
d1 = user_info.copy()
print(d1)
d1.clear()
print(d1)