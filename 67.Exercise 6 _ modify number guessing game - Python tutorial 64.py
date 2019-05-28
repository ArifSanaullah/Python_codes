#67.Exercise 6 _ modify number guessing game - Python tutorial 64


import random
winning_num = random.randint(1,100)
#winning_num = 45
trynum = 1
guess_num = int(input("plaese guess a number between 1 and 100: "))
GameOver = False
while not GameOver:
    if guess_num == winning_num:
        print(f"cong.....! you guessed the right number in {trynum} times")
        GameOver = True
    else:
        if guess_num > winning_num:
            print("too high")
            trynum += 1
            guess_num = int(input("plaese again guess a number between 1 and 100: "))
        else:
            print("too low")
            trynum += 1
            guess_num = int(input("plaese again guess a number between 1 and 100: "))