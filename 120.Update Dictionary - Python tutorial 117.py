# 120.Update Dictionary - Python tutorial 117
user_info = dict(
    name = 'arif',
    age = 24,
    surname = 'sanaullah',
    cgpa = 3.6,
    fav_movies = ["prince of percia","captain jack sparrow"],
    fav_tunes = ["fairy tales","rising sun"]
)
#print(type(user_info))
#if a key is already in existing dict then update method will update the value of existing key from new dict
more_info = dict(
    name = 'ali',
    state = "punjab",
    hobbies = ["coding", "movies watchng"]
)
user_info.update(more_info)
print(user_info)