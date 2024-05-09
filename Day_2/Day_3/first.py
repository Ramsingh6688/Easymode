## iterate over a list of numbers 

list = [21, 34, 56, 53, 87]
length = len(list)

for i in range(length):
    print(list[i])
    
    
## iterate over a list of strings 


list = ["anuj", "ankit", "ram", "manoj"]
length = len(list)

for i in range(length):
    print(list[i])
    

###     iterate over a tuple of integers and print the square of each integer.

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
square = print([i**2 for i in tuple])


## loop to find the average of all numbers in a list.

list = [2, 4, 8, 12, 16, 20]
sum = 0
for i in list:
    sum = sum + i
avg = sum/len(list)
print("the average is =", round(avg,2))
    



##iterate over a dictionary and find the key associated with the maximum value.

dict1 = {'juice': '10', 'grill': '40', 'corn': '90'}
max_key = next(iter(dict1))
for value in dict1:
    if dict1[value] > dict1[max_key]:
        max_key = value
            
    
###, where each tuple contains a student's name and their score, and print the names of students who scored above 90.


dict1 = [('anu', 57),('ram',96),('ankit',99)]
max = -999999999

 
 
## all strings in a list into a single string.


list1 = ["my", "self", "ram"]
 
ans = ' '
for i in list1: 
   
  ans = ans+ ' '+ i
print(ans)
 
 
 ##a for loop to find the intersection of two sets.
 
set1 = {1, 2, 4, 56, 78}
set2 = {3, 2, 43, 56, 36, 98}
 
print(set1.intersection(set2))
 
 
##while loop

###a while loop to find the sum of all numbers divisible by 3 or 5 within a given range.

#def sum_divisible_by_3_or_5(n):

 #sum = 0
 #for i in range(n):
        
    #if i % 3 == 0 or i % 5 == 0:
    
     #sum += i
     #print(sum_divisible_by_3_or_5(10))  
     #print(sum_divisible_by_3_or_5(20))  
     
     
##a while loop to reverse a list in-place (without using the reverse() method).

list1 = [10, 20, 30, 40]
start = 0
end = len(list1) -1
while start < end :
    start = 1
    end -= 1
    print(list1)

    


##a while loop to find the union of two sets
