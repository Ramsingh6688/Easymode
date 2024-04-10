p = int(input("Enter the first number:"))
q = int(input("Enter the second number:"))

oper = input("Enter the type of operation you want(+,-,*,/,%):")

result = 0

if oper == "+":
    result = p+q 
    
elif oper == "-":
    result = p-q
    
elif oper == "*":
    result = p*q
    
elif oper == "/":
    result = p//q # Integer Division
    
elif oper == "%":
    result = p%q
    
else:
    print("Invalid input ")

print("your answer is :", result)
