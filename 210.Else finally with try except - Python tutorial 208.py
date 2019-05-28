# 210.Else finally with try except - Python tutorial 208

while True:
    try:
        age = int(input('please enter your age: '))  # seven
    except ValueError:
        print("invalid input...")

    except:
        print("unexpected error...")
    else:
        print(f"user input is {age}")
        break
    finally:
        print("this is finally result...")

if age < 18:
    print("you can\'t play the game...!")
else:
    print("you can play the game...!")
# print("you can\'t play the game...!" if age < 18)