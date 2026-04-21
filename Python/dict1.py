person = {
    "name": "Balasekhar",
    "age": 25,
    "city": "Vizag"
}

print(person.keys())
print(person.items())

#Add a new key, value

person["phone"] = 123
person.update({"country": "India"})
print(person)
