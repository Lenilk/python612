num_input=int(input())
for i in range(num_input,0,-1):
    print(" "*(num_input-i),end="")
    print("*"*(1+2*(i-1)))