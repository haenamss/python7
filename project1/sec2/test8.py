#if와 복수 조건
jum = [90, 80, 100] #파이썬의 열거형(이더레이터)
#모든 점수가 80점 이상이면, 합격
if(jum[0]>=80 and jum[1]>=80 and jum[2]>=80 ):
    print("합격")

#세과목중 한과목이라도 90점 이상이면 과목우수
if(jum[0]>=90 or jum[1]>=90 or jum[2]>=90):
    print("과목우수")
else:
    print("")

avg = float((jum[0]+jum[1]+jum[2])/3)
print("평균 : ", avg)

if(avg>=90):
    if(avg>=96):
        print("A+")
    elif(avg>=93):
        print("A0")
    else:
        print("A")




