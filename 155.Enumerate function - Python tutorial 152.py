# 155.Enumerate function - Python tutorial 152

# enumerate functions

# how to do this without enumerate functions

names = ["abc","def","ghi","jkl","mno"]
pos = 0
# for name in names:
#     print(f"{pos}---->{name}")
#     pos += 1



# with enumerate functions

# for pos,name in enumerate(names):
#     print(f"{pos}---->{name}")


# practice task

def find_target(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return (pos)
    return -1

print(find_target(names,"mnof"))




# find = lambda l,target : pos if names[pos] == target else -1
#
# print(find(names,"mno5"))
