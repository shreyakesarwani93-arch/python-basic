# prime number
num=int(input("Enter the number:"))
for i in range(2,num//2+1):
    if num%1==0:
        print("Not prime number")
        break
    else:
        print("Prime number")

