class Student:
    def __init__(self, name, rollnum, marks):
        self.name=name
        self.rollnum=rollnum
        self.marks=marks
    
    def talk(self):
        print("Hello, I am: ", self.name)
        print("My roll num: ", self.rollnum)
        print("I got:", self.marks)


s1 = Student("Bala", 12, 33)
print(s1.marks)
s1.talk()
