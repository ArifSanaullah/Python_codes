# 215.Read Text Files - Python tutorial 213

# read method
# open method
# readfile-------> to read a file line by line
# seek method
# tell method ----> it is used when we want to know where my cursor is right now
# readline method
# readlines method
# close method
# by default opening mode is read mode of files
# data descripter-----> name,closed


f = open(r"F:\Ustaad\audio files\video files\document files\textfile.txt")
print(f.name)

# lines = f.readlines()
# for line in lines:
#     print(line, end="")
# print(len(lines))
# print(f"{f.read()}")
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f"after reading the file tell method {f.tell()}")
# print(f"after reading the file seek method")
# f.seek(0)
# print(f" after seek method {f.tell()}")
# print(f.read())
print(f.closed)
f.close()
print(f.closed)
