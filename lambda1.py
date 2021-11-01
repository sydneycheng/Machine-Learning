import os

clear = lambda: os.system("cls")
clear()


# def remainder(num):
#     return num % 2

remainder = lambda num: num % 2
print(type(remainder))
print(remainder(5))

product = lambda x,y: x * y
print(product(2,3))

##example 1
def myfunction(num):
    return lambda x: x * num

#result10 is a function created from a lambda
    #10 = num
result10 = myfunction(10)
result100 = myfunction(100)

#this is the same as this
#result10 = lambda x: x * 10

print(result10(9))
print(result100(9))

##example 2
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)   #this is n
mytripler = myfunc(3)   #this is n

print(mydoubler(11))   #this is a
print(mytripler(11))   #this is a

##Higher Calling Functions

numbers = [2,4,6,8,10,3,18,14,21]

#get numbers > 7
filtered_list = list(filter(lambda num: (num > 7), numbers))
print(filtered_list)

#mapped function - applies function to every element in an iterable
mapped_list = list(map(lambda num: num % 2, numbers))
print(mapped_list)  #puts answers in 0s and 1s


x = lambda a: a + 10

print(x(5))
x = lambda a,b,c: a + b + c
print(x,5,6,7)

def addition(n):
    return n + n

#traditional method (function, iterable)
numbers = [1,2,3,4]
result = map(addition, numbers)
result = map(lambda x:x + x, numbers)
print(list(result))


