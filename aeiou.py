str_input=list(input())
aeiou_list=["a","e","i","o","u"]
aeiou_group=[]
str_group=[]
for i in range(len(str_input)):
    if str_input[i] in aeiou_list:
        count=0
        str_list=""
        for j in range(1,(len(str_input))-i):
            if str_input[i+j] in aeiou_list:
                count+=1
                
        if count!=0:
            for k in range(count+1):
                str_list+=str_input[i+k]
                str_input[i+k]="0"
            aeiou_group.append(str_list)
            
        else:
            aeiou_group.append(str_input[i])
print(aeiou_group)
for i in range(len(aeiou_group)):
    str_list1=""
    for j in aeiou_group[i]:
        if j in aeiou_list:
            str_list1+=j
    str_group.append(str_list1)
print(str_group)