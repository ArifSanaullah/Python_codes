# 118.Looping and In Kyeword in dictionary - Python tutorial 115
user_info = dict(
    name = 'arif',
    age = 24,
    surname = 'sanaullah',
    cgpa = 3.6,
    fav_mavies = ["ghi","jkl"],
    fav_tunes = ["abc","def"]
)
if 'names' in user_info:
    print('present')
else:
    print("not present")

if 'arif' in user_info.values():
    print('present')
else:
    print("not present")
for i in user_info:
    print(i)
for i in user_info.values():
    print(i)
user_info_keys = user_info.keys()
print(type(user_info_keys))
for i in user_info:
    print(user_info[i])
user_items = user_info.items()
print(user_items)
print(type(user_items))
for key, value in user_items:
    print(f"key is {key} and value is {value}.")