sentance = "I am in Visakhapatnam"
#o/p: "Visakhapatnam in am I"

reverse_str = ""
words = sentance.split()
for word in words:
    reverse_str = word +" "+ reverse_str
    print(reverse_str)

#print(reverse_str)

joined_words = " ".join(words)
print(joined_words)