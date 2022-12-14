play=True
while (play):
    # input number
    num_input=int(input("ป้อนตัวเลข เพื่อหาจำนวนเฉพาะ ทั้งแต่ 0 ถึง "))
    if num_input<0:
        print("ข้อมูลผิดพลาด")
    else:
        # function for search prime number of range
        def Prime(number):
            prime_list=[]
            for i in range(number+1):
                count=0
                for j in range(1,i+1):
                    if i%j==0:
                        count+=1
                if count==2:
                    prime_list.append(i)
            return prime_list
        #create varieble for prime number
        Prime_number=Prime(num_input)
        #Display length of prime number
        print("มีจำนวนเฉพาะ ทั้งหมด ",len(Prime_number),"ตัว ดังนี้",end=" ")
        #Display prime number
        for i in Prime_number:
            print(i,end=" ")
        play=False
