num_input=int(input())
str1=""
str_space=(" "*num_input)
for i in range(num_input,0,-1):
    str1+=str_space
    for j in range(i):
        str1+=" "
    for k in range((num_input-i)+1):
        str1+="* "
    if i!=1:
        str1+="\n"
str2=""
str3=""
for i in range(num_input,0,-1):
    str3=""
    for j in range(i):
        str3+=" "
    for o in range((num_input-i)+1):
        str3+="* "
    for j in range((i*2)-2):
        str3+=" "
    for o in range((num_input-i)+1):
        str3+="* "
    str2+=str3
    if i>1:
        str2+="\n"
print(str1)
print(str2)