'''
def Multiplication(Num):
    for i in range(1, 11):
     print(Num, " * ", i, "=", Num * i)

Num = int(input("Enter a number: "))
for i in range(1, Num + 1):
    Multiplication(i)
    print('')
'''


X=int(input("Enter a number: "))
Y=int(input("Enter a number: "))
for X in range(X,Y+1):
    if X % 4 == 0 and X % 100 != 0 or X % 400 == 0:
        print(X, 'Leapyear')
    else:
        print(X, 'Not Leapyear')


