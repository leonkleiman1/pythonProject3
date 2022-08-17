count_valid=0
grade=int(input("please enter grade:"))

while grade>=0 and grade<=100:
    count_valid+=1
    if count_valid==5:
        print("to many trials")
        break
    grade = int(input("please enter grade:"))
else:
    print("leon")