import json


try:
    with open('now.json', 'r') as file:
         DicData = json.load(file)
         print(DicData)

except Exception as error:
    print(error)

finally:
    print("Done")
