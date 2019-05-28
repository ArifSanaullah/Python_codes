# 164.Advance min() and max() - Python tutorial 162

numbers = [1,2,3,4,5,7,9]
print(f"this is simple max {max(numbers)}")
print(f"this is simple min {min(numbers)}")

def name_len(item):
    return len(item)

names = ['arif_1', 'sana_12','abid_123']
print(max(names,key = name_len))
students_dict = {
    'arif' : {"score" : 901, "age" : 21},
    'sana' : {"score" : 95, "age" : 28},
    'abid' : {"score" : 99, "age" : 25}
}

print(max(students_dict , key= lambda item : students_dict[item]['age']))

students_list = [
    {"name" : "abc",'score' : 123, 'age' : 21},
    {"name" : "def",'score' : 124, 'age' : 22},
    {"name" : "ghi",'score' : 125, 'age' : 23}
]
print(max(students_list , key=lambda item: item.get('score')))