def my_function(a,b,c):    #Local Function
    n = (a+b+c)*2
    return n
import random              #libary Function

print("For A :")

numbers = []
for _ in range(3):
    numbers.append(random.randint(1, 100))
    print(numbers)
A = my_function(numbers[0],numbers[1],numbers[2])
print("A:",A)

print(""
    
      "")

print("For X :")


numbers1 = []
for _ in range(3):
    numbers1.append(random.randint(1, 10))
    print(numbers1)
X = my_function(numbers1[0],numbers1[1],numbers1[2])
print("X:",X)