def money(day,hr,work):
    if (day.lower()).title()=="Sunday":
        return hr*(3*work)
    else:
        return hr*((3/2)*work)
print("โปรแกรมคำนวณค่าแรง")
print("day <space> hour <space> normalwage")
print("**day: Sunday Monday Tuesday wednesday Thursday Friday Saturnday**")
day,hr,work=[str(x) for x in input().split()]
print("เงินที่จะได้ทั้งหมด",money(day,int(hr),int(work)),"บาท")