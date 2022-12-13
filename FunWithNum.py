digit_input=int(input())
num_input=[int(x) for x in input().split()]
num_input.sort()
print(num_input)
list_num=[]
for i in range(len(num_input)):
    num_list=num_input
    print(num_input)
    str1=""
    print(i)
    str1+=str(num_input[i])
    num_list.pop(i)
    for j in num_list:
        str1+=str(j)
    list_num.append(int(str1))
print(min(list_num))
    


