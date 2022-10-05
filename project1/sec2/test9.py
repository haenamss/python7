#반복문 : 해당 조건이나 상황이 만족될 때 반복 수행
i = tot = 0     # i = 0
                # tot = 0
while(i<=10):
    tot+=i      #tot=t0t+i
    i+=1        #i=i+1
print("0~10 합계 : ", tot)

#짝수의 합계
i = tot = 0
while(i<=100):
    if(i%2==0):
        tot+=i      #tot=t0t+i
    i+=1            #i=i+1
print("0~100까지 짝수의  합계 : ", tot)

i = 0
tot = 0
while(i<=100):
    tot+=i
    i+=2
print("짝수 합 : ", tot)

#홀수의 합계
i = tot = 0
while(i<=100):
    if(i%2!=0):
        tot+=i
    i+=1
print("1~100까지 홀수의 합계 : ", tot)

i=1
tot=0
while(i<=100):
    tot+=i
    i+=2
print("홀수 합 : ", tot)
