# 80.Chater 4 Exercise 2 - Python tutorial 77
#take a string from user aa a input
#reverse the string
#and match the originala and reversed strings
#if both are same return true else return false
#uncomment each code block one by one but outputs are the same for both


#def is_palindrom(word):
#    if word == word[::-1]:
#        return True
#    else:
#        return False


def is_palindrom(word):
    return word == word[::-1]
print(is_palindrom('madam'))
print(is_palindrom('arif'))