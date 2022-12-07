print("----------------------------------------------------")
print("--------------โปรแกรม คำนวณจำนวนวันศุกร์ที่ 13-----------")
print("------------------input in one line----------------")
print("ชนิดปี：ปีปกติ（1） ปีอธิกาุรทิน（0） เว้นวรรค วันที่เริ่มต้นของปี เว้นวรรค ปี ค.ศ.")
print("วันที่เริ่มต้นของปี 1:Sunday 2:monday 3: tuesday 4: wednesday 5: thursday 6: Friday 7:Saturday")
typeYear,initDay,year=[int(x) for x in input().split()]
#ตรวจสอบว่าเป็นอธิกสุรทินหรือไม่
if typeYear==0:
    day=366
elif typeYear==1:
    day=365
# เก็บจำนวนวันทั้งหมด
dayOfYear=[int(s) for s in range(initDay-1,day+(initDay)-1) ]
# สร้างดิกไว้กำหนดเดือนและจำนวนวันของเดือน
dict_month={}
# เดือน
month=["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤภาคม","มิถุนายน","กรกฏาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
# กำหนดจำนวนวันของแต่ละเดือน
for i in month:
    if "คม" in i:
        dict_month[i]=31
    elif "ยน" in i:
        dict_month[i]=30
    else:
        if typeYear==0:
            dict_month[i]=29
        elif typeYear==1:
            dict_month[i]=28
# ใส่จำนวนวนที่ของปีในแต่ละเดือน
for i in dict_month:
    dayofmonth=[]
    for j in range(dict_month[i]):
        dayofmonth.append(dayOfYear[j])
    # ลบแต่ละวันออกจากลิสต์ของปี เพื่อไม่ให้ซ้ำ
    for k in dayofmonth:
        dayOfYear.remove(k)
    dict_month[i]=dayofmonth
# ระบุว่าวันที่เท่าไหร่เป็นวันอะไร
for i in dict_month:
    sevenday=[]
    for k in dict_month[i]:
        k%=7
        sevenday.append(k)
    dict_month[i]=sevenday
dict_friday=dict_month
for i in dict_month:
    friday=[]
    for k in dict_month[i]:
        # เก็บวันศุกร์ทั้งหมดไว้ในดิกชั่นเนรี่แต่ละเดือน
        if k==5:
            friday.append(dict_month[i].index(k)+1)
            dict_month[i][dict_month[i].index(k)]=10
    dict_friday[i]=friday
# หาวันที่13 ที่เป็นวันศุกร์
fridaymount=[]
for i in dict_friday:
    if 13 in dict_friday[i]:
        fridaymount.append(i)
print("วันที่ 13 วันศุกร์ มี ",len(fridaymount),"เดือน ได้แก่")
for i in fridaymount:
    print("เดือน",i,end=" ")
print()
# นับจำนวนของวันศุกร์ที่ 13ของปีนี้
count=0
for i in dict_month:
    for j in dict_month[i]:
        if j==13:
            count+=1
print("ซึ่งมีทั้งหมด",count,"ครั้ง")
