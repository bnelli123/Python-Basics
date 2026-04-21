# def is_palindrome(s):
#     try:
#         for i in range(len(s) // 2):
#             if s[i] != s[len(s) - i - 1]:
#                 print("Not a Palindrome")
#                 return
#         print("Palindrome")
#     except:
#         print("No error")

def split_palindrom(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    s=input("Enter string: ").strip()
    split_palindrom(s)








