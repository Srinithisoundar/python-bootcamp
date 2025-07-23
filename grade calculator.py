totmarks = int(input("Enter Total marks: "))
obtmarks = int(input("Enter obtained marks: "))
c = obtmarks/totmarks*100
if c >= 90:
    print("your grade is A+")
elif c >= 75:
    print("your grade is A")
elif c>=60:
    print("your grade is B")
elif c>=40:
    print("your grade is C")
else:
    print("your grade is F")
