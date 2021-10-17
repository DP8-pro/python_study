import string

lst = list(string.ascii_letters + string.digits)

#print first symbol of list
print(lst[0])

#print the last symbol of list
print(lst[-1])

#print 3rd from beginning and 3rd from the end symbols
print(lst[2])

print(lst[-3])

#make slice of first 10 symbols
print(lst[:10])

#print only symbols with index, which divides on 3 without remaining
print(lst[::2])

#print only integer values from list
int_lst = []
for i in lst:
    try:
        int_lst.append(int(i))
    except:
        pass
    
print(int_lst)
print(int_lst[::-1])


#convert base list into string
print("-".join(lst))  # String from list

