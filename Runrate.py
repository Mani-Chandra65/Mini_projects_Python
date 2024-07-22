print("Welcome!!\nThis is a runrate calculator!\n")
totOv=int(input("Enter total number of overs:"))
print("Total number of overs=",totOv)
comOv=0
ovLef=totOv
finRun=0
while ovLef != 0:
    print("\n")
    print("Completed overs:",comOv,"\nOvers left:",ovLef)
    i=0
    totRun=0
    runs=[]
    currRR=0
    currOv = comOv+1
    while i<6:
        c=1
        currun=int(input("Enter runs scored in this ball:"))
        runs.append(currun)
        totRun+=currun
        currRR2=(currRR+((totRun/(i+1))*6))/currOv
        print("Ball Runrate:",currRR2)
        c+=1
        i+=1
        finRun+=totRun
        currRR=(finRun/currOv)
    print("Total runs in this over:",totRun)
    print("RunRate=",currRR)
    comOv+=1
    ovLef-=1
    print("\n")
    print(runs)