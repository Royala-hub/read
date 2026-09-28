"""
#Number 1

n=int(input("Please enter your exam score: "))
if n>=90:
    print("A")
elif 75<=n<=89:
    print("B")
elif 50<=n<=74:
    print("C")
else:
    print("F")
"""
##################################
"""
#Number 2

n=int(input("n= "))
for i in range(1,11):
    k=n*i
    print(k,end=" ")
"""
#################################
password="Hello123"
n=input("Please enter the password: ")
if n==password:
    print("Successful login!")
else:
    i=2
    while n!=password:
        if i<=3:
            n=input("Please enter the password again: ")
        else:
            print("Please try later")
            break
        if n==password:
            print("Successful login!")
            break
        i=i+1