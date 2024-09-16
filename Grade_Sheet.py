mark = input("Enter your mark:")
print(mark)
if int(mark)>=80:
    print("CGPA: A+")
elif int(mark)>=70:
   print("CGPA: A")
elif int(mark)>=60:
   print("CGPA: B")
elif int(mark)>=55:
   print("CGPA: C")
elif int(mark)>=50:
  print("CGPA: D")
elif int(mark)>=40:
    print("CGPA: E")
else:
    print("Field")
