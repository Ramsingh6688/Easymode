age = int(input("Enter the age"))

if age <0:
    print("Invalid age")
elif age <18 & age >0:
    print("child")
elif age >=18 & age <60:
    print("adult")
elif age >60 & age <160: 
    print("senior citizen") 
else:
    print("Invalid age")
