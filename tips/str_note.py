#str 
"""
[::]
find()
count()
upper()
lower()
split()
strip()
replace()
startswith()
endswith()

"""
#use for string:'',"","""""""
# cannot change after create
# ordered
# iterable
# has index

s = "Hello Python"

# print(s[4])
# print(s[-3])

# #s[2] = "D"
# #print(s[2]) #error because it cannot be changed

# #[start:end:steps], end still excluded,if steps is negative means from back to front
# print(s[0:5:1]) #get Hello
# print(s[-6:13:1]) #get Python
# print(s[2:5:-1]) #get nothings because the direction is conflict
# print(s[-1:-7:-1]) #nohtyP 
# print(s[::-1]) #nohtyP olleH

#find(), from the start, to find the place of the word
print(s.find("H")) #0
print(s.find("He")) #0
#only the first elements

#count(),count the exist time of one alphabet
print(s.count("l")) #2

#upper(), upper the text
print(s.upper()) #HELLO PYTHON

#lower(), lower the text
print(s.lower()) #hello python

#split(), split the words into a list based on your column input
print(s.split(" ")) #['Hello', 'Python']
print(s.split("o")) #['Hell', ' Pyth', 'n']

#strip(), remove the space on the start and end 
print(s.strip()) #Hello Python

#replace(),replace an elements from the text to be other elements
print(s.replace("o","e")) #Helle Pythen

#startswith(), to check is the text start from specific elements, return True False
print(s.startswith('H')) #True
print(s.startswith('h')) #False
print(s.startswith('Hello')) #True

#endswith(), to check is the text end from specific elements, return True False
print(s.endswith("n")) #True
print(s.endswith("on")) #True
print(s.endswith("Pytho")) #False

print(s) #will not change
