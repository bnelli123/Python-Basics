#%%
# class Student:
#     ''' This is developed by Bala'''
#     #Variables
#     # Methods

# print(Student.__doc__)
# help(Student)


#%%
class Student:
    print("Hello")
    city = "Vizag"
    def __init__(self): #Constructor
        print("Hello, I am from Constructor")
        self.name="Durga"
        self.rollnum=101
        self.marks=90
    
    def talk(self):
        print("Hello, I am: ", self.name)
        print("My roll num: ", self.rollnum)
        print("I got:", self.marks)

Student() #Object
s1 = Student() #s1: Reference Variable
print(s1.name)
print(s1.city)

# %%
class Student():
    def __init__(self, x, y, z):
        self.name = x
        self.rn = y
        self.marks = z

s3=Student("Bala", 1,2)
print(s3.rn)

        
