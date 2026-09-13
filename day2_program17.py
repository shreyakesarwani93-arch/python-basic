#prime number
n = int(input("Enter the number: "))
f = 0

for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = 1
        break

if f == 0:
    print("Prime")
else:
    print("Not prime")
