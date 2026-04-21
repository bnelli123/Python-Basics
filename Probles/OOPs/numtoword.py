'''
Given a number N, the task is to convert every digit of the number into words.

Examples: 
Input: N = 1234 
Output: One Two Three Four 
Explanation: 
Every digit of the given number has been converted into its corresponding word.

Input: N = 567 
Output: Five Six Seven 
'''
# n = int(input().strip())
# #0-9

# words_upto_9 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# if n <=9:
#     print(words_upto_9[n])
# else:
#     print("Enter number between 0 and 9")

#%%
#Input: N = 567 
#Output: Five Six Seven
N = int(input().strip())
words_upto_9 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word = ""

for n in str(N).split():
    word = word + words_upto_9[int(n)]

print(word)


