# 148.-- Kwargs - Python tutorial 145

# kwargs (also known as key value arguments)
# but always read kwrags in python


# def func(**kwargs):
#     print(kwargs)
# func(first = "arif", last = "khan")


# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# func(first="arif", last="khan")


# dict unpacking
# d = {"name" : "arif", "age" : 24, "grade" : "graduation"}
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# func(**d)


# extra arguments passing except **kwargs
def func(name, **kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}, {name}")
func(name="arif",first="arif", last="khan")