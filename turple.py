//Modifying a Tuple

a = (3, 4, 5)
b = [3, 4, 5]

b[0] = 10
print(b)

a = list(a)   
a[0] = 12
a = tuple(a)  
print(a)

_____________________________________________________

//Tuple Modification

a = (3, 4, 5)
b = [3, 4, 5]

b[0] = 10
print(b)

a = (12,) + a[1:]
print(a)

_____________________________________________________

//Indexing and slicing

a = [2, 24, 10, 12, 13, 3, 4, 34, 9, 8]
print(a[0])
print(a[1 : 9 : 2])
print(a[-3])

______________________________________________________

//Printing using specific Index number

name = "ANKUR"
name[0] = "A"

______________________________________________________

//Palindrome

s = "madam"
print(s == s[::-1])


