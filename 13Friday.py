typeYear,initDay,year=[int(x) for x in input().split()]
if typeYear==0:
    day=366
elif typeYear==1:
    day=365
dayOfYear=[int(s) for s in range(initDay,day+(initDay)) ]
dict_month={}
month=["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤภาคม","มิถุนายน","กรกฏาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
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
print(dict_month)
for i in dict_month:
    dayofmonth=[]
    for j in range(dict_month[i]):
        dayofmonth.append(dayOfYear[j])
    for k in dayofmonth:
        dayOfYear.remove(k)
    dict_month[i]=dayofmonth
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
        if k==5:
            friday.append(dict_month[i].index(k)+1)
            dict_month[i][dict_month[i].index(k)]=10
    dict_friday[i]=friday
count=0
for i in dict_month:
    for j in dict_month[i]:
        if j==13:
            count+=1
print(count)
