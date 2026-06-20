#2. 定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。

#user input
userinput = input("Insert a words: ") 

#function for count the vowels
def c_vowels(words):

    count = 0

    for i in words:
        
        if i in {'a','e','i','o','u','A','E','I','O','U'}: #or in"aeiouAEIOU"

            count +=1

    return count

#print the number of vowels
print(c_vowels(userinput))
