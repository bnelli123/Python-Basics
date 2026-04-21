def greet():
    print("Hello")

def greet_with_name(name):
    print("Hello", name)

def add(a,b):
    c = a + b
    return c

def greet_default(name="Jhansi"):
    print("Hello", name)

def keyword_args(name, age):
    print(name, age)

def total(*args):
    return sum(args)

def person(name, *args):
    print("Name:", name)
    print("Other:", args)

def kwargsfun(**kwargs):
    print(kwargs)

def accessKwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
greet()
greet_with_name("Bala")
result=add(3,4)
print(result)
greet_default("Sam")
keyword_args("Bala", 23)
keyword_args(age=23, name="Suman")
keyword_args("suman", age=23)


print(total(2,3,4,5))
print(total(9,0,23,34,5,3))

person("Alice", "Bala", 23, True, 2.3)
kwargsfun(name = "Alice", age = 23, real = True)
accessKwargs(name = "Alice", age = 23, real = True)