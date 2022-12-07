num_input=int(input())
for i in range(num_input,0,-1):
    print(" "*(i-1),end="")
    print("*"*(1+2*(num_input-i)))
