# 150.chapter 11 exercise 2 - Python tutorial 147

#
# def ret_capital(*args):
#     empty = str[args]
#     c = args.captalize()
#     empty.append(c)
#     print(empty)
#     for i in args:
#         j = str(i)
#         j[0].upper()
#         empty.append(j)
#     return empty
# print(ret_capital(['arif',"khan"]))
# l = ['arif',"khan"]
# for k in l:
#     # m = k[0].upper()
#     o = k.capitalize()
#     print(o)
    # for n in k:
    #     k[0] == m
    # print(k)


def func(*args):
    s = str(args)
    # print(type(s))

    for k in s:
        cap = s[2].upper()
        s[2] == cap
        print(cap)

l = ['arif',"khan"]
print(func(*l))