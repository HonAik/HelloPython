"""
● 根据提供的学生成绩单,完成如下需求:
name    id   BM  BE BC
Reynolds 001 67  92  63
Dorcas   002 47  86  45
Ray      003 59  76  57
Nick     004 75  53  66

1. 计算每个学生的总分、各科平均分,然后一并输出出来。

2. 统计各科成绩的最低分、最高分、平均分,并输出。

3. 查找成绩优秀(平均分大于90)的学生,并输出。

"""
#create a tuple:
students = (
    ("Reynolds","001",67,92,63),
    ("Dorcas","002",47,86,45),
    ("Ray","003",89,96,87),
    ("Nick","004",75,53,66),
    ("Danny","005",67,64,84)
)

#1:calculate
#写法1：
# for i in students: #now i also a tuple
#     total = i[2] + i[3] + i[4]
#     avg = total/3

#     print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {total} {avg:.1f} ") #.1f means this is float number and only one decimal number is fine

#写法2：
for name,id,bm,be,bc in students:
    total = bm+be+bc
    avg = total/3
    print(f"{name} {id} {bm} {be} {be} {total} {avg:.1f} ")

#2:find
#get the scores from the tuple:
bm = [i[2] for i in students ]
be = [i[3] for i in students ]
bc = [i[4] for i in students ]

#find
#bm
bm.sort()
print(bm[0])
print(bm[-1])
print(sum(bm)/len(bm))

#be
print(min(be))
print(max(be))
print(sum(be)/len(be))

#bc
print(min(bc))
print(max(bc))
print(sum(bc)/len(bc))

#3
print("Students who above 90 scores")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total/3

    if avg > 90:
        print(f"{i[0]} {i[1]} {avg:.1f}")