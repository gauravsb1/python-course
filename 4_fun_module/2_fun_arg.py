# 1- positional argument

def add1(a,b):
    return a+b


print(add1(2,3))





# 2- default argument

def add2(a,b , plus=1):

    return a+b+plus

# print(add2(2,3))

print(add2(2,3,3)) #override





# 3- keyword argument

def data(age , name):

    return f"my name is {name} and age is{age}"

print(data(name="gv", age= 25))




    