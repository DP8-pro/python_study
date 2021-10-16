import string

#Generate string with lowercase and uppercase alphabet plus numbers
text = string.ascii_letters + string.digits

#Print 1st symbol of string
print(text[0])

#Print last symbol
print(text[-1])

#Print 3rd from beginning and 3rd from the end symbols
print(text[2])

#Print 3rd from the end symbols
print(text[-3])

#Slice first 8 symbols
print(text[:8])

#Print only symbols with index, which divides on 3 without remaining
print(text[::3])

#Print the symbol of the middle of the string text
print(text[int(len(text)/2):int(len(text)/2)+1])

#Reverse text using slice
print(text[::-1])
