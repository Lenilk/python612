ABC_input=str(input("ใส่ \"A\" \"B\" \"C\""))
#ลูกบอลตำแหน่งเริ่มต้น ที่ 1
a=1
b=0
c=0
#ใช้ ตัวแปร d มารับค่า
d=0
ABC_list=["A","B","C"]
Error=True
for i in ABC_input:
    if i in ABC_list:
        if i=="A":
            d=a
            a=b
            b=d
        elif i=="B":
            d=c
            c=b
            b=d
        elif i=="C":
            d=a
            a=c
            c=d
    else:
        print("โปรดใส่ตัวอักษร A B C")
        Error=False
        break
if Error!=False:
    if a==1:
        print("1")
    elif b==1:
        print("2")
    elif c==1:
        print("3")