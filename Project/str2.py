"""
1. 输入一个字符串,判断该字符串是否是回文(两边对称)
"""

w = input("Insert a sentences: ")
new_w = []
# new_w = w[::-1]

# if new_w == w:
#     print("This is palindrome")
# else:
#     print("This is not palindrome")

print(f"{w} is palidrome" if new_w == w[::-1] else f"This is not palidrome")