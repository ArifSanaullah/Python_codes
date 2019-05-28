# 119.Add and delete data from dictionaries - Python tutorial 116
user_info = dict(
    name = 'arif',
    age = 24,
    surname = 'sanaullah',
    cgpa = 3.6,
    fav_mavies = ["ghi","jkl"],
    fav_tunes = ["abc","def"]
)
user_info["fav_songs"] = ['song1', 'song2']
print(user_info)
#pop takes at least one argu and it returns given type of the key value pair in the dict
popped_ = user_info.pop("fav_tunes")
print(f"popped item is {popped_}")
print(user_info)
#popped_item takse no argu and removes the last key value pair in the dict and it returns tuple
popped_item = user_info.popitem()
print(f"popped item from  popitem is {popped_item}")
print(user_info)