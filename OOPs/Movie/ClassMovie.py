class Movie:
    def __init__(self, title, hero, heroine):#We can take arguments with any name
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("MovieName: ", self.title)
        print("HeroName: ", self.hero)
        print("HeroineName: ", self.heroine)

while True:
    title = input("Enter Movie Name: ").strip()
    hero = input("Enter Hero Name: ").strip()
    heroine = input("Enter Heroine Name: ").strip()
    m = Movie(title, hero, heroine)
    list_of_movies = []
    list_of_movies.append(m)
    print("Movie successfully added")
    option=input("Do you want to add one more movie [Yes|No]:").strip()
    if option.lower() == "no":
        break
print(list_of_movies) # [<__main__.Movie object at 0x102976120>, <__main__.Movie object at 0x102964410>]
print("All movie info..")
print('*' * 20)

for i in list_of_movies:
    i.info()
    print('-'*10)