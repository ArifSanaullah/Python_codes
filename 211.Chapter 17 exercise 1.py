# 211.Chapter 17 exercise 1
# 212.Chapter 17 exercise 1 solution

def devide(num1 , num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("devision by zero is not allowed...")
    except TypeError as arr:
        print(arr)
    except:
        print("unexpected error")


print(devide("1" , 5))
print(devide(5 , 0))
print(devide(10 , 2))
