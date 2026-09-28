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
#When we type characters in a terminal or console, the operating system treats our keystrokes as a sequence of raw characters (bytes/text)
#input() simply reads this standard input stream until we press Enter, collecting everything as a literal sequence.
#Programmers can enter anything-numbers, letters, symbols, spaces, or empty lines. By returning a string every time, Python guarantees a single, predictable data type.
#Python is a strongly typed language, meaning it enforces strict rules about what operations are valid between different data types.
#The + and * operators mean completely different things for strings versus numbers