# 169.Function returning function - Python tutorial 167

def o_func():
    def i_func():
        print("its inner function")
    return i_func
var = o_func()
var()

def o_func2():
    msg = 'this is returnd by o_func2'
    def i_func2():
        msg2 = 'this is returned by i_func2'
        print(f"{msg2}")
    return i_func2()
    print(f"{msg}")
    return o_func2()
var2 = o_func2()
