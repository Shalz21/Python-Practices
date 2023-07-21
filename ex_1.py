#1)
a=10
b=7
print(a+b)

#2)
l=12
b=6
print("Area of rectangle=",l*b)

#3)
c=40
f=(c*9/5)+32
print("Fahrenheit=",f)

#4)
num=12
print("Even" if num%2==0 else "Odd")

#5)
a="new"
b="line"
print(a+b)



#6)
x=10
y=12
z=14
avg=(x+y+z)/3
print(avg)

#7)
year=2016
if year%4==0:
    print("leap year")
else:
    print("not a leap year")

#8)
a="morning"
b='good'
a,b=b,a
print(a,b)

#9)
from math import pi
r=7
area=pi*(r^2)
circumference=2*pi*r
print("Area of a circle:",area)
print("Circumference of a circle:",circumference)

#10)
a="malayalam"
if a[::-1]==a:
    print("Palindrome")
else:
    print("Not a Palindrome")

#branching and iteration
#1)
age=23
if age<18:
    print("You are a minor")
else:
    print("You are an adult")

#2)
a=-5
if a>0:
    print("Positive Number")
elif a<0:
    print("Negative Number")
else:
    print("Zero")

#3)
x=9
if x%3==0:
    if  x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
elif x%5==0:
    print("Buzz")


#4)
a=[12,25,3,6,131,133]
print(max(a))

#5)
a=3
if a==1 or a== 2 or a== 12:
    print("Winter")
elif a==3 or a== 4 or a== 5:
    print("Spring")
elif a== 6 or a== 7 or a==8:
    print("Summer")
else:
    print("Autumn")

#6)

for i in range(1,101):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

#7)
num=5
fact=1
for i in range(1,6):
    fact=fact*i

print("The factorial of 5 is",fact)

#8)
num=8
first_num=0
second_num=1
for i in range(num):
    next_num=first_num
    first_num=second_num
    second_num=next_num+first_num
print(second_num)

#9)
a="We are playing"
a.lower()
data="aeiou"
vowels={}.fromkeys(data,0)
for i in a:
    if i in data:
        vowels[i]+=1
for character in vowels:
    print(character,":",vowels[character])

#string methods
#beginner level
#1)
a="Good Morning"
print(len(a))

#2)
a='python'
print(a.capitalize())

#3)
a="What is your name?"
print(a.endswith("?"))

#4)
a="python programming"
print(a.split())

#5)
a="I like kiwi but i love apple more than kiwi"
print(a.replace("kiwi","papaya"))

#6)
x="Hello World"
print(x.startswith("Hello"))

#7)
a="python programming"[0:3]
print(a)

#8)
a="programming"
print(a.isalpha())

# 9)
a="programming"
data={}.fromkeys(a,0)
for i in a:
    if i in data:
        data[i]+=1
for alpha in a:
    print(alpha,"=",data[alpha])

#10)
a="ButteR bEaN caFe "
print(a.lower())


#intermediate level

#1)
a="apple123"
print(a.isalnum())

#2)
a="python"
print(a.index("h"))

# 3)
a="butter bean cafe"
a.lower()
vowels="aeiou"
data={}.fromkeys(vowels,0)

for i in vowels:
    if i in a:
        data[i]+=1

for character in vowels:
    print(character,"=",data[character])

#4)

#5)
a="cherry"[::-1]
print(a)

#6)
a="new line"
print(a.replace(" ",""))

#7)

#8)
a="new line"
print(a.replace(" ","_"))

#9)

#10)
a="orange"
x=''.join(sorted(a))
print(x)

