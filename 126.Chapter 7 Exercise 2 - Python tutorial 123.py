# 126.Chapter 7 Exercise 2 - Python tutorial 123
info = {}
name = input("what is your name: ")
age = input("what is your age: ")
fav_movie = input("what is your faovourite movie seperated by a coma: ").split(",")
fav_song = input("what is your faovourite song seperated by a coma: ").split(",")
info["name"] = name
info["age"] = age
info["fav_movie"] = fav_movie
info["fav_song"] = fav_song
for key,value in info.items():
    print(f"{key} : {value}")