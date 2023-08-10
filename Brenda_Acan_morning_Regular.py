import re
def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
    
email1="acanbrenda217@gmail.com"
email2="acan.brenad217@gmail.com"

print(validate_email(email1))
print(validate_email(email2))

#generators and iterators
#yield
def factorial(n):
    if n==0:
        yield 1
    else:
        yield n*factorial(n-1)  
for i in range (1,10):
    print (factorial(i))


#Example3
#Generate function that yields  the square of numbers from 1 to 10
def square():
    for i in range(1,10):
        yield i**2

#Create an iterator that yields the square of numbers from 1 to 10
squares_iterator =square()
#Print the first 5 square numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))

#Decorators
def my_decorator(func):
    def inner():
        print("I am inner")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("I am outer")

outer_decorator()                   


