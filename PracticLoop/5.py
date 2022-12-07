num_input=int(input())
for i in range(num_input,0,-1):
    for j in range(num_input-i):
        print(" ",end="")
    print("*"*i)