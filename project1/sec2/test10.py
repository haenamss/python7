#for 반복문
data = [90,80,100,60,70]
a=tot=0

for i in data:
    a+=1
    tot+=i
    print("점수 : ", i)
print("총점 : ", tot)
print("평균 : ", float(tot/a))

jum = [(100,80,70),(80,90,70),(70,50,60),(90,95,95)]
for (kor, eng, mat) in jum:
    tot = kor+eng+mat
    avg = float(tot/3)

    hak = ""
    if(avg>=90):
        hak = "A"
    elif(avg>=80):
        hak = "B"
    elif(avg>=70):
        hak = "C"
    elif(avg>=60):
        hak = "D"
    else:
        hak = "F"
    print("총점 : ", tot)
    print("평균 : ", avg)
    print("학점 : ", hak, "\n")


tot=0
for i in range(1, 101):  #range : 범위
    tot+=i
print("1~10 합계 : ", tot)

data1 = [40, 65, 70, 90, 85]        #list
data2 = [num *2 for num in data1]   #for~in을 list에 내포 # data1값에 2를 곱함
data3 = [num *2 for num in data1 if num%2==0]    #for~in을 list에 내포 # data1 값중에 짝수인 것만 2를 곱함
print(data2)
print(data3)






