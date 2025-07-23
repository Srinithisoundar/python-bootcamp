total_marks = int(input("enter your total marks: "))
obtained_marks = int(input("enter your marks: "))
percentage = (obtained_marks/total_marks)*100
print("you scored",percentage,"%")
print("you scored",round(percentage,2),"%")
print(f"you scored {percentage:.2f}%")
print("you scored {:.2f}%".format(percentage))
print("you scored",(int(percentage)),"%")
print(f"you scored {int(percentage)}%")
