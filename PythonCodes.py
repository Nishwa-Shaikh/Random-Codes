#Swap two numbers
'''n=int(input("Enter any 2 digit number: "))
if n>9:
    n=str(n)
    print(n[::-1])
    n=int(n)
elif n>0 and n<=9:
    print(f"0{n}")
else:
    n=str(n)
    print(n[0]+n[:0:-1])'''
    
#Checking if a number is prime or not
'''n=int(input("Enter an integer: "))
count=0
for i in range(2, n+1):
    if n%i==0:
        count+=1
if count==1:
    print("prime number")'''

#Calculating power
'''base=int(input("Enter base: "))
power=int(input("Enter power: "))
for i in range(1, power+1):
    Answer=base**i
print(Answer)'''

#Check if a number is palindrome
'''n=int(input("Enter number: "))
n=str(n)
if n[::]==n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#Printing prime numbers between 2 intervals
'''num1 = int(input("Enter any number: "))
num2 = int(input("Enter another number: "))
for i in range(num1+1, num2):
    count=0
    for j in range(2, i):
        if i%j==0:
            count+=1
            break
    if count==0 and i>1:
        print(f"{i} is prime.")'''

#GCD
'''Num1=int(input("Enter any number: "))
Num2=int(input("Enter any number: "))
while Num2!=0:
    Num1, Num2=Num2, Num1%Num2
print(f"The GCD is {Num1}")'''

#LCM
'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a, b = num1, num2
while num2 != 0:
    num1, num2 = num2, num1 % num2
GCD = num1
LCM = (a * b) // GCD
print(f"The LCM of {a} and {b} is {LCM}")'''

#Factorial
'''n=int(input("Enter any number: "))
count=1
for i in range(1, n+1):
    count*=i
print (count)'''

#Fibonacci series
'''a, b=0,1
n=int(input("Enter number: "))
if n==1:
    print(a)
elif n==2:
    print(a, b)
else:
    print(a, b, end=" ") 
    for i in range(3, n+1):
        next=a+b
        print(next, end=" ") 
        a, b= b, next'''

#Armstrong number
'''Sum=0
n=int(input("Enter any number: "))
n=str(n)
for i in n:
    i=int(i)
    Sum+=i**len(n)
if Sum==int(n):
    print(f"{n} is an armstrong number")
else:
    print("Not an armstrong")'''

#Perfect number
'''SUM=0
n=int(input("Enter number: "))
for i in range(1, n):
    if n%i==0:
        SUM=SUM+i

if SUM==n:
    print(f"{n} is a perfect number")
else:
    print("Not a perfect number")'''

#Strong number:
'''SUM=0
num=int(input("Enter number: "))
STR=str(num)
for i in STR:
    i=int(i)
    fact=1
    for j in range(1, i+1):
        fact=fact*j
    SUM=SUM+fact
if SUM==num:
    print("STRONG number!")
else:
    print("try another number")'''
    
#Swapping values by function
'''def Swap(num1, num2):
    print(f"Num1 before Swap is {num1}\nNum2 before swap is {num2}")
    num3=num2
    num2=num1
    num1=num3
    print(f"Num1 after swap is {num1}\nNum2 after swap is {num2}")
Swap(2,4)'''

#Factorial using reccursion
'''def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)
result = fact(5)
print(result)'''

#Fibonacci using recursion
'''a, b= 0, 1
n=int(input("Enter value: "))
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1))+(fib(n-2))
for i in range(n):
    print(f"{fib(i)} ", end='')
FIB=fib(n)
print(FIB)'''

#armstrong number using function

'''def Armstrong():
    n=int(input("Enter number: "))
    n_str=str(n)
    SUM=0
    for digit in n_str:
        digit=int(digit)
        SUM+=digit**len(n_str)
    if SUM==n:
        print("Armstrong number")
    else:
        print("Not an armstrong number")
Armstrong()'''

#Reverse a number using functions
'''def Reverse():
    num=int(input('Enter number: '))
    num_str=str(num)
    reverse=num_str[::-1]
    int_reverse=reverse
    print(int_reverse)
Reverse()
'''
#Count the digits using function
'''def Count():
    COUNT=0
    Num=int(input("Enter number: "))
    Num_str=str(Num)
    for digit in Num_str:
        digit=int(digit)
        COUNT+=1
    print(COUNT)
Count()'''

#Write a function to calculate nCr, Combination
'''def Combination():
    Num1=int(input("Enter number1: "))
    Num2=int(input("Enter number2: "))
    if Num1<=0 or Num2<=0:
        print("Numbers should be greater than 0")
    if Num2>Num1:
        print("Num2 should be less than Num1")
    else:
        def fact(n):
            if n == 1 or n == 0:
                return 1
            else:
                return n * fact(n - 1)
    COMB=fact(Num1)/(fact(Num2)*(fact(Num1-Num2)))
    print(COMB)
Combination()'''

#Calculate sum of array elements:
'''SUM=0
numbers=(input("Enter all the numbers you want to sum seperated by spaces: ")).split()
for nums in numbers:
    SUM+=int(nums)
print(SUM)'''

#Reverse an array
'''N=input("Enter data seperated by spaces: ").split()
Processed_data=[]

for data in N:
    try:
        data=int(data)
        Processed_data.append(data)
    except ValueError:
        Processed_data.append(str(data))
RN=Processed_data[::-1]
print(RN)'''

#Count frequency of an element
'''count=0
N=input("Enter data seperated by spaces: ").split()
DATA=input("Enter item you want to know: ")
for data in N:
    if data!=DATA:
        continue
    else:
        count+=1
print(f"{DATA} is repeated {count} times")'''

#print a matrix
'''Mat=[]
row1=[]
for i in range(1,4):
    row1.append(i)
Mat.append(row1)
row2=[]
for j in range(4, 7):
    row2.append(j)
Mat.append(row2)
for row in Mat:
    print(row)'''

#Addition of 2 matrices
'''Mat1=[]
row1=[]
for i in range(1,4):
    row1.append(i)
Mat1.append(row1)
row2=[]
for j in range(4, 7):
    row2.append(j)
Mat1.append(row2)
Mat2=[]
row12=[]
for i in range(1, 4):
    row12.append(i)
Mat2.append(row12)
row22=[]
for j in range(4, 7):
    row22.append(j)
Mat2.append(row22)
mat3=[]
for i in range(len(Mat1)):  # loop over the rows
    row = []
    for j in range(len(Mat1[0])):  # loop over the columns
        row.append(Mat1[i][j] + Mat2[i][j])
    mat3.append(row)
for row in mat3:
    print(row)'''

#Finding len without str len
'''count=0
Word=input("Enter any word: ")
for i in Word:
    count+=1
print(count)'''

#Remove all duplicates from a string
STR=input("Enter string: ")
STRING=''
seen=set()
for char in STR:
    if char not in seen:
        STRING+=char
        seen.add(char)
print(STRING)