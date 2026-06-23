name = "Satyam Shorrf"
age = 20
PI = 3.14

print ("My name is", name)
print ("I am", age, "years old")
print ("The value of PI is", PI)



print (type(name))

print (type(age))

print (type(PI))


num = 3

isPrime = True

print (type(num))
print (type(isPrime))

Hey = None
print (type(Hey))



#Out # My name is Satyam Shorrf


'''
this is a multi line comment
in python


'''


'''

Keywords in Python

False None as assert break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield








'''



#Sum of two numbers

first_number = 23
second_number = 45 

sum = first_number + second_number

print("The sum is:", sum)

''' 
Variables in Python

'''


name = "Satyam"
age = 20

PI = 3.14

print ("My name is", name)
print ("I am", age, "years old")


#Operators in Python

#artithmetic operators


a = 10
b = 5

c = a + b
print ("The sum is:", c)


d = a - b
print ("The difference is:", d)

e = a * b
print ("The product is:", e)

f = a / b
print ("The division is:", f)

g = a % b
print ("The remainder is:", g)

print (a**b)


#Relational operators / comparison operators

a = 10
b = 5

print (a > b)
print (a < b)
print (a >= b)
print (a <= b)

print (a == b)
print (a != b)
print (a is b)

print (a is not b)

print (a in [1, 2, 3, 4, 5])
print (a not in [1, 2, 3, 4, 5])

print(6 > 99)

print(6 < 99)


#Assignment operators

a = 10
a = a + 5
print (a)

a += 5
print (a)
a -= 5
print (a)
a *= 5
print (a)
a /= 5
print (a)
a %= 5
print (a)


a = 39
a *= 5
print (a)

a **= 5
print (a)


#Logical operators

#And Operators

var = False 


print((5 > 3 ) and (3 > 2))  # True
print((5 > 3 ) and (3 > 8))  # True

x = 3 
x += 5 
print(x)

# Operator Precedence 
'''
()
**
*, /, % 
+, -
==, !=, >, >=, <, <= 

not 
and 
or 




'''

# Type Conversion

ans1 = int(8 +40.9) #casting
ans2 = 8 + 39.9 #conversion


print(ans1, type(ans1))
print(ans2, type(ans2))

val = str("123")

print(val, type (val))




# User Input

username = input("enter your name:")
print(username)

a = input("Enter First Number:- ")
b = input("Enter Second Number:- ")

sum =(a+b)
print(sum)