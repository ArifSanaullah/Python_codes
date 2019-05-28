# 125.Word Counter Dictionary - Python tutorial 122
def word_count_in_dict(string):
    count = {}
    for character in string:
        count[character] = string.count(character)
    return count
print(word_count_in_dict("sanaullah"))