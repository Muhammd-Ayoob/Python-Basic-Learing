number= int(input("Enter an Integer \n"))
if number>10:
    if number%2==0:
        print("Number is Greater than 10 and Even")
    else:
        print("Number is Greater than 10 and Odd")
elif number<10:
    if number%2==0:
        print("Number is Less than 10 and Even")
    else:
        print("Number is Less than 10 and Odd")
else:
    print("Number is Equal to 10 i-e Even")