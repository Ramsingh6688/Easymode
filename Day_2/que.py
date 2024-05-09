# Mylist = [1, 2, 3, 4, 5]
# print(Mylist)

# if Mylist == 3:
#  print("yes its present")

# else:
#     print("No its not there")
    
    
    
# #touple

# my_tuple = (10, 20, 30, 40, 50, 45, 33)
# length = len(my_tuple)
# print(length)

# if length % 2 == 0:
#     print("The number is even")
# else: 
#     print("The number is odd")

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
        
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was Debited")
#         print("Total balance =", self.get_balance())
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount , "was credited")
#         print("Total balance =", self.get_balance())
        
#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000 , 123446)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(5)
# acc1.credit(1500000000000000000000000)
# acc1.get_balance()
        
        
# def no_letters_and_digits(char):
#     num_letters = 0
#     num_digits = 0
#     for i in char:
#         if char.isalpha():
#             num_letters += 1
#         elif char.isdigit():
#             num_digits += 1
        
#     return num_letters, num_digits
# input_string = input(" Enter a string ")
# num_letters, num_digits = no_letters_and_digits(input_string)
# print("Alpha->", num_letters, "and number ", num_digits)
    
    
    
# ##4

# def sum_of_odd_numbers (start, stop):
#     a = 0
#     for i in range (start , stop +1):
#         if i % 2 !=0:
#             a += i
#         return a
#     start = 1
#     stop = 10
#     result = sum_of_odd_numbers(start, stop)
#     print("sum of odd number between ", start, "and", stop,"is", result )
    
##7

def Lcm(a,b):
    greater = max(a,b)
    smallest = min(a,b)
    
    for i in range(greater, a*b+1 , greater):
        if i % smallest ==0:
            return i
if __name__ == '__main__':
    a = 12 
    b = 15
print("Lcm of " , a, 'and' , b, 'is', Lcm(a,b))
        
    
def lcm(a,b):
    greater = max(a,b)
    smallest = min(a,b)
    
    for i in range(greater, a*b+1, greater):
        if i % smallest ==0:
            return i
if __name__ == '__main__':
    a = 12
    b = 15
    print("lcm of", a, 'and' , b, 'is', lcm(a,b))
    
            
