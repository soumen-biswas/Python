'''
import random

random_number = random.randint(1, 100)
print(random_number)
'''


import datetime
today = datetime.datetime.now()
print(today)
today = datetime.date.today()
print(today)


'''
import time

curr = time.ctime()
print(curr)
'''

'''
import random #buidin function

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 1000))

print(numbers)

max_number=float('-inf')
for i in numbers:
    if i > max_number:
        max_number = i
print("Max_number is :",max_number)
'''