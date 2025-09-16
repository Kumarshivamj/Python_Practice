a = input("Enter the String: ")
b = ""
for i in a:
    b = i + b
if a == b:
    print(f"{a} is pelindrome")
else:
    print(f"{a} is not pelindrome")