num_input=int(input())
for i in range(1,num_input+1):
    for j in range(num_input+1-i,1,-1):
        print(" ",end="")
    print("*"*i)