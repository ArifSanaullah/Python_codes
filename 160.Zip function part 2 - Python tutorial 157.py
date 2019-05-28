# 160.Zip function part 2 - Python tutorial 157

l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_l = []

l = [(1,2),(3,4),(5,6),(7,8)]

print(f"this is simple zip unpacking {list(zip(*l))}")

li1,li2 = list(zip(*l))
print(li1)
print(li2)

for pair in zip(l1,l2):
    max(pair)
    new_l.append(max(pair))
print(new_l)