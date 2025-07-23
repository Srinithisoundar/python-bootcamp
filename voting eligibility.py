name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
if age >=18:
    print(f"Hi,{name},you can vote")
else:
    print(f"Sorry,{name}, you need to wait {18-age} more yrs.")
