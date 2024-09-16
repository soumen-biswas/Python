'''
result = 0
for num in range(1,50):
    result += num
    print(num)

print(result)
'''

'''
numbers = [0,7,1,4,2,9,3,5,8,6]

max_num = float('-inf')
for i in numbers:
    if i > max_num:
        max_num = i

print(max_num)
'''
'''
result = 0
for i in range(1,101):
    if i % 3 == 0 and  i % 5 == 0:
        print(i)
        result += i

print("The sum is:",result)
'''
'''
A=float(input())
B=float(input())

average=(A*3.5+B*7.5)/(3.5+7.5)

print(f"MEDIA = {average:.5f}")
'''
w = int(input())

if w % 2 == 0 and w > 2:
    print("YES")
else:
    print("NO")
