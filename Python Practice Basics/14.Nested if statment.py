#Nested if statment

grade=int(input("Enter your Marks:"))
if grade>=90:
    print("You got grade A")
else:
    if grade>=80:
        print("you got grade B")

    else:
        if grade>=70:
            print("you got grade C")
        else:
            if grade<=60:
                print("Sorry you fail !!")
