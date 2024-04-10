### Linear structure

list1 = [1, 2, 4, 6 , "anuj","ram","vikash", 23, 45, 70,["hello","hii"]]
print(list1)

list2 = [12,34,65,98.89]
list1.extend(list2)
print(list1)

print(list1.index(["hello","hii"]))
print(list1)

fruits = ["mango","apple","orange"]
fruits.insert(10,"list1")
print(list1)

list3 = [3,5,7]
list1.append(list3)
print(list1)

list4 = ["anuj", "ankit", "sandeep", "pradeep"]
print(list4.count("ankit"))

list1.remove("anuj")
print(list1)

list2.sort()
print(list2)



tuple1 = (2, 4, 6, 8, 13,["anuj", "ankit", "ashok"], 34, 90)
print(tuple1)
tuple1[4]


### NON LINEAR STRUCTURE


dict1 = {"ankit": 23 , "acer": 10,"ankit": 56 , "anuj": 34}
print(dict1)

dict2 = {"pradeep": 10, "sunil":25}
print(dict2.values())

dict2.update(dict1)
print(dict2)

dict2= list(dict1.items())
print(dict2)

A= {"safar": 45, "trip": 32, "politics": 67}
print(A.get("safar"))

print(dict1.keys())

dict1.pop("acer")
print(dict1)

print(A.popitem())

A.setdefault(" ", 50)
print(A)


set1 = {"pooja", "ashok", "pradeep", "ashok"}
print(set1)

set1.add("raj")
print(set1)

set1.pop()
print(set1)

set1.clear()
print(set1)