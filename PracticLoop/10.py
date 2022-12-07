num_input=int(input())
for i in range(num_input-1,-1,-1):
    print(" "*i,end="")
    print("* "*(num_input-i))