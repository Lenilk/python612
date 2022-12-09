num_input=int(input())
for i in range(num_input*2,1,-1):
    if i>num_input:
        print(" "*((i-num_input)-1),end="")
        print("* "*(((num_input*2)-i)+1))
    else:
        print(" "*((num_input-i)+1),end="")
        print("* "*(i-1))