# 209.Try , Except - exception handling, python tutorial 207

# exception
# try exception else finally


while True:
    try:
        age = int(input('please enter your age: ')) # seven
        break
    except ValueError:
        print("invalid input...")
    except:
        print("unexpected error...")

if age < 18:
    print("you can\'t play the game...!")
else:
    print("you can play the game...!")