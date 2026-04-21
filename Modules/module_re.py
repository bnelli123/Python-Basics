import re

text = "My name is Balsekhar Nelli 894523 12334 123343 Balasdf"

result = re.search(r"\d+", text)
print(result.group())

result = re.findall(r"\d+", text)
print(result)

#Replace text
new = re.sub(r"Balsekhar", "Jhansi", text)
print(new)

new2 = re.sub(r"\bBal\w*", "Jhansi",text)
print(new2)