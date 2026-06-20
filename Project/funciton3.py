#3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。
# example:{Reynolds,48,23,97,23,14}

#列表：list
userinput = []

#for name
name = input("Insert a name: ")
userinput.append(name)

#for scores:

for i in range(5):
    #put the userinput into scores and then append it intp the userinputlist then do again
    scores = int(input(f"Insert nunmbers{i+1}: "))
    userinput.append(scores)


#it became [Reynolds,1,2,3,4,5]

#funciton for calculation of scores
def scores_calculation(scores_list):
    
    #filter str:
    pure_list = [i for i in scores_list if isinstance(i,(int,float))]
        
        #find max scores
    highS = max(pure_list)

        #find min scores
    minS = min(pure_list)

        #find avg scores
    avg = round(sum(pure_list)/ len(pure_list),1)

    return highS,minS,avg

#print()
HS,MS,AS = scores_calculation(userinput)
print(f"{userinput[0]} has HS ={HS}, MS ={MS}, AS ={AS}")

