# 140.Dictionary Comprehension - Python tutorial 137
square = {f"Square of {num} is": num ** 2 for num in range(1 , 11)}
for k , v in square.items():
    print("{}: {}".format(k , v))


string = "abcdefghabacdes"
word_count = {f"occurence of '{char}' is": string.count(char) for char in string}
for k,v in word_count.items():
    print(f"{k} : {v} time(s)")