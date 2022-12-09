num_input=int(input())
for i in range(num_input,0,-1):
    print(" "*(i-1),end="")
    print("*",end="")
    print(" "*(2*(num_input-i)-1),end="")
    if num_input-i>0:
        print("*")
    else:
        print()