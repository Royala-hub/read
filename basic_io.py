name=input("Enter your name: ")
age=input("Enter your age: ")
num=input("Enter your favourite number: ")
age=int(age)
num=int(num)
new_age=age+10
new_num=num**2
if num%2==0:
    k="even"
else:
    k="odd"
print(f"Hi {name}! In 10 years you'll be {new_age}. Your name squared is {new_num}, and it's {k}")
