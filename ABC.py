a=[int(x) for x in input().split()]
ABC_input=str(input())
#สร้างตัวแปรสตริงสำหรับรับค่า
str1=""
#เรียงจากน้อยไปมาก
a.sort()
A=a[0]
B=a[1]
C=a[2]
for i in ABC_input:
    if i=="A":
        str1+=str(A)+" "
    elif i=="B":
        str1+=str(B)+" "
    elif i =="C":
        str1+=str(C)+" "
    else:
        print("โปรดใส่ ABC")
print(str1)