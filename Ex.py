'''
today = input("Enter the day: ")
today = today.title()
public_holiday = input("It is a public holiday? (Yes/No): ")
public_holiday = public_holiday.capitalize()
is_sick_today = input("Are you sick today? (Yes/No): ")
is_sick_today = is_sick_today.capitalize()

if today == ("Sunday" or "saturday") or public_holiday=="Yes" or is_sick_today =="Yes" :
    print("No office today")
else:
    print("You have to go to office")
'''

def meets_requirements(price,brands,colors,mileage):
    budget = 20000
    my_brands = ["Toyota","BMW"]
    my_colors = ["Blue","Green","red","black","yellow"]
    maximum_mileage = 30000

    if (price <= budget ) and ( brands in my_brands ) and (colors in my_colors) and (mileage <= maximum_mileage) or (price <= budget//2 and 30000 < mileage <=40000) :
        return True
    else:
        return False

price = int(input("Enter your price: "))
brands = input("Enter your brands: ")
colors = input("Enter your colors: ")
mileage = int(input("Enter your mileage: "))

if meets_requirements(price,brands,colors,mileage):
    print("You are good to go!")
else:
    print("Sorry, you are not good to go!")