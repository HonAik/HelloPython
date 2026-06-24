# foundational implementation of folder:
# open, read, write, close


#open a folder
f = open(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\resources\file1.txt","r",encoding="utf-8")

#read from a folder
# content = f.read() # read all
# print(content)

#readline()
contentlist = f.readlines() # read one line
for line in contentlist:
    print(line.strip()) #strip() to remove \n

#close a folder
f.close()
