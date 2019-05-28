# 184.List vs Generators - Python tutorial 182
import time
# list vs generators
# memory useag,time
# when to use list or generator


t_Start = time.time()
l = [i**2 for i in range(1,1000000)]
# for i in l:
#     print(i)
t_end = time.time()
print(f"this is for list {(t_end)-(t_Start)}")

# print(l)

t_Start_g = time.time()
g = (i**2 for i in range(1,1000000))
# for i in g:
#     print(i)
t_end_g = time.time()
print(f"this is for generators {(t_end_g)-(t_Start_g)}")


# print(g)