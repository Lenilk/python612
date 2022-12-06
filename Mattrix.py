#รับค่ามิติของแมตตริก
y,x=[int(x) for x in input().split()]
num_list1=[]
num_list2=[]
sum_list=[]
count=0
#รับค่าแมตตริกที่ 1
for i in range(y):
    b=[int(i) for i in input().split()]
    num_list1.append(b)
#รับค่าแมตตริกที่ 1
for i in range(y):
    d=[int(k) for k in input().split()]
    num_list2.append(d)
#นำแต่ละตำแหน่งมาบอกกัน
for i in range(y):
    for j in range(x):
        sum_list.append(num_list1[i][j]+num_list2[i][j])
#แสดงผลลัพธ์
for i in range(y):
    for j in range(x):
        print(sum_list[count],end=" ")
        count+=1
    print()
