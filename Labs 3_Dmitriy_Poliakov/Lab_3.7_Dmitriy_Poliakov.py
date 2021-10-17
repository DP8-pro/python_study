import string

#Generate two sets with not unique numbers and few symbols
set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

#Print 1st set
print(set1)

#2nd set
print(set2)

#Print intersection
tpl_intersection = tuple(set1.intersection(set2))

#Print intersection
print(tpl_intersection)

#Print difference between two sets
tpl_diff = tuple(set1.difference(set2))
print(tpl_diff)

#Slice first 3 symbols from first tuple
print(tpl_intersection[:3])

#Print only numbers from second set
print(set(string.digits).intersection(set2))

#Reverse tuple using slice
print(tpl_intersection[::-1])

#Convert both tuples into list
print(list(tpl_intersection), list(tpl_diff))

