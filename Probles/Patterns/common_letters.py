#s1 = "NAINA"
#s2 = "REENE"
#N
def common_letters():
    str1 = input("Enter string1: ")
    str2 = input("Enter string2: ")

    #Remove duplicates
    s1 = set(str1)
    s2 = set(str2)

    print(s1)
    print(s2)

common_letters()


def common_letters2(s1, s2):
    return set(s1) & set(s2)

print(common_letters2("apple", "grape"))