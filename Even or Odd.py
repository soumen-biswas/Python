Num = input("Enter a number: ")
if int(Num) % 2 == 0 and int(Num) > 0:
    print(Num, " is Even and Positive")
elif int(Num) % 2 != 0 and int(Num) > 0:
    print(Num, " is Odd and Positive")
elif int(Num) % 2 == 0 and int(Num) < 0:
    print(Num, " is Even and Negative")
elif int(Num) % 2 != 0 and int(Num) < 0:
    print(Num, " is Odd and Negative")
