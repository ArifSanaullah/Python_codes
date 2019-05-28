# 83.Default Parameters - Python tutorial 80
def user_info(first_name, last_name, age):
    print(f"person's first name is {first_name}")
    print(f"person's last name is {last_name}")
    print(f"persons age is {age}")

user_info('arif','sanaullah',25)

#remember that default parameter can only be last one in the fucntion. means in thenfollowing code age can be set to any default value
#but first_name and last_name can not be set to default value. to set them to default we need to move them in the last of the
#of definition of funcion e.g. def user_info(age, first_name = "unknown", last_name = "unknown")
def user_info(first_name,age, last_name="unknown"):
    print(f"person's first name is {first_name}")
    print(f"person's last name is {last_name}")
    print(f"persons age is {age}")

user_info('arif',25)