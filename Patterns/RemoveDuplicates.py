# s1 = "AABBBBBCCDDZZZSSFGWEEDKKLLIIIJJ"
# s2 = []

# for ch in s1:
#     if ch not in s2:
#         s2.append(ch)

# print((''.join(s2)))
s1 = "AABBBBBCCDDZZZSSFGWEEDKKLLIIIJJ"
s2 = ""

for ch in s1:
    if ch not in s2:
        s2 = s2 + ch

print(s2)

