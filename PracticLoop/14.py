num_input=int(input())
for i in range(1,num_input+1):
    print(" "*(i-1),end="")
    print("*",end="")
    print(" "*(2*((num_input-i))-1),end="")
    if i!=num_input:
        print("*")