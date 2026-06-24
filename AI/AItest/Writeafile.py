#open a folder
f = open("file2.txt","w",encoding="utf-8")

#write a file
f.write("《敕勒歌》（南北朝·乐府民歌）\n")
f.write("敕勒川，阴山下。\n")
f.write("天似穹庐，笼盖四野。\n")
f.write("天苍苍，野茫茫。\n")
f.write("风吹草低见牛羊。\n")

#close a folder
f.close()

#with as
# with open("file2.txt","w",encoding="utf-8") as f:
#     f.write("《敕勒歌》（南北朝·乐府民歌）\n")
#     f.write("敕勒川，阴山下。\n")
#     f.write("天似穹庐，笼盖四野。\n")
#     f.write("天苍苍，野茫茫。\n")
#     f.write("风吹草低见牛羊。\n")
#it is better to use with as to close a folder and avoid the risk of forgetting to close a folder,unlike try except finally