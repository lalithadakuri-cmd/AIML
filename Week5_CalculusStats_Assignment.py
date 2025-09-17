name = print(input("Enter name: "))
sci = int(input("Enter Science Marks: "))
mat = int(input("Enter Maths Marks: "))
if ((sci > 50) and (mat > 50)) == True:
    print(f"{name}, you are selected!")
else:
    print(f"Sorry, {name} you are not selected")
