num_input=int(input())
for i in range(1,num_input*2):
    if i<=num_input-1:
        print("*"*i)
    else:
        print("*"*((num_input*2)-i))
