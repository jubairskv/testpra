
#reverse number
'''
a=[1,2,3,4]
a.reverse()
print(a)
'''
#reverse string
'''
a="jubair"
b=a[::-1]
print(b)
'''
#reverse the word using string
'''
a="hi i am jubair"
b=a[::-1]
print(b)
'''
#Reverse string using recursion
'''
def reverse(s):
    if len(s)==1:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("enter the string: ")
a=reverse(s)
print("reverse string",a)
'''     
#reverse and separate word:
'''
a="hi i am jubair"
b=a.split(' ')
print(b)
c=b[::-1]
print(c)
d=' '.join(c)
print(d)
'''
#sort a string in alphabet order
'''
a="jubair"
b=list(a)
print(b)
b.sort()
print(b)
c=' '.join(b)
print(c)
'''
#reverse list using iterative method:
'''
a=[1,2,3]
for i in range(len(a)-1,-1,-1):
     print(a[i],end="")
'''
#reverse string using for loop:
'''
a="chinu"
b=''
for i in a:
    if i in a:
       b=i+b
print(b)
'''
#length of string without build in function:
'''
a="jubair"
b=0
for i in a:
    if i in a:
        b=b+1
print(b)
'''
#method 2:
'''
a="jubair"
b=len(a)
print(b)
'''
#count word in the given string
'''
a="hi i am juabir"
b=len(a.split())
print(b)
'''
#input="i am python developer"
#output="I Am Python Developer"
'''
a="i am python developer"
x=a.title()
print(x)
'''
#input="i am python developer"
#output="I am python developer"
'''
a="i am python developer"
x=a.capitalize()
print(x)
'''
#convert two dicionary into singel dictionary
'''
a={'a':1}
b={'b':2}
a.update (b)
print(a)
'''
#convert two list into singel set:
'''
a=[1]
b=[2]
x=a+b
print(x)
y=set(x)
print(y)
'''
#combine two list
'''
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
'''
#matrix into single list:
'''
a=[[1,2,3],[4,5,6]]
b=[]
for i in a:
    b.extend(i)
print(b)
'''
#add two list into singel dictionary:
#mehod 1
'''
a=['a','b','c','d']
b=[1,2,3,4]
c=dict(zip(a,b))
print(c)
'''
#method 2 using for loop:
'''
a=['a','b','c','d']
b=[1,2,3,4]
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
print(c)
'''
#inpu="python"
#output="pythsn"
#method 1
'''
a="python"
x=a.replace('o','s')
print(x)
'''
#method 2:
'''
a="python"
for i in a:
    if i in "o":
        print('s',end="")
    else:
        print(i,end="")
    
'''
#Array Right Rotation :
'''
def right_rotation(l,n):
    for i in range(n):
        t=l[len(l)-1]
        for j in range(len(l)-1,0,-1):
            l[j]=l[j-1]
        l[0]=t
    return l
l=[10,20,30,40,50]
n=2
print(right_rotation(l,n))
'''
#array left Rotation
'''
def Left_rotation(l,n):
    for i in range(n):
        t=l[0]
        for j in range(0,len(l)-1):
            l[j]=l[j+1]
        l[len(l)-1]=t
    return l
l=[1,2,3,4,5,6]
n=2
print(Left_rotation(l,n))
'''
#remove duplicate from list:
#method 1:
'''
a=[1,1,2,3,4,5,5,6,7,8,8,9]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)

'''
# user run time input method:
'''
n=int(input("enter the interval :"))
a=[]
b=[]
c=[]
for i in range(n):
    v=int(input("enter :"))
    a.append(v)
print(sorted(a))
for i in a :
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print("orignal :",b)
print("duplicate:",c)
'''
#method 2:
'''
a=[1,1,2,3,4,5,5,6,7,8,8,9]
print(list(set(a)))
'''
#remove multiple duplicate number:
'''
a=[1,2,2,2,2,4,5,6,6,6,7]
b=[]
for i in a:
    if i in b:
        b.remove(i)
        continue
    b.append(i)
print(b)
'''
#remove duplicate :
'''
a=[1,2,3,4,5]
b=[2,3,4,5,6]
c=[]
for i in range(len(a)-1,0,-1):
    for j in range(len(b)):
        if a[i]==b[j]:
            a.remove(a[i])
            b.remove(b[j])
            break
print(a)
print(b)
for i in b:
    a.append(i)
print(a)
'''
#remove dulicate in two list:
'''
a=[1,2,3,4,5]
b=[3,4,5,6,7,8]
for i in a:
    for j in b:
        if i==j:
            print(i)
            break
'''
#method 2:
'''
a=[1,2,3,4,5]
b=[3,4,5,6,7,8]
a,b=list(set(a)-set(b)),list(set(b)-set(a))
c=list(set(a)-set(b))+list(set(b)-set(a))
print(a)
print(b)
print(c)
'''
#remove duplicate string:
'''
a=input("Enter the string :")
b=''
c=''
for i in a:
    if i not in b:
        b=b+i
    else:
        c=c+i
print(b)
print(c)
'''
#Repeating element:
'''
a=[1,1,2,2,3,3,4,4,4,6,7,7,8]
for i in a:
    if a.count(i)==2:
        print("First repeating number is:",i)
        break
else:
    print("NO repeating number")
'''
#first non-repeating number:
'''
a=[1,1,2,2,3,3,4,4,4,6,7,7,8]
for i in a:
    if a.count(i)==1:
        print("First non-repeating number is:",i)
        break
else:
    print("NO repeating number")
'''
#first non-repeating string:
'''
from collections import Counter
s="jjubair"
a=Counter(s)
for i in s:
    if a[i]==1:
        print("First non-repating string is:",i)
        break
else:
    print("NO repeating number")
'''

#Non-repeating without build-in-function:
'''
a="jjubbairr"
d=dict()
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
for i in d:
    if d.count(i)==1:
        print(i)
        break
''' 
#method 2:
'''
a="jjubair"
##print(list(a))
for i in a:
    if a.count(i)==1:
        print("first non-repeating string is:",i)
        break
else:
    print("NO repeating number")
'''
#add two list
'''
a=[1,2,3,4]
b=[5,6,7,8]
for i in b:
    a.append(i)
print(a)
'''
#method 2 add two list:
'''
a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(c)
'''
#integer and string remove string only:
'''
a="1234jubair"
for i in a:
    if i.isalpha():
        print(i)
    else:
        print('',end='')
'''
#integer and string remove number only:
'''
a="1234jubair"
for i in a:
    if i.isdigit():
        print(i)
    else:
        print("",end="")
'''
#missing element in list:
'''
a=[1,2,3,5,6,8,9]
for i in range(1,10):
    for j in a:
        if i==j:
            break
    else:
        print(i,end=" ")
        
'''
#find min,max,sum,avg,middle value of an array:
'''
a=[1,2,3,4,5,6,7]
b=a[0]
c=a[0]
s=0
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
    if a[i]<c:
         c=a[i]
print("Max:",b)
print("Min:",c)
for i in a:
    s=s+i
    avg=s/len(a)                    #avg=sum of product/total no of product
    mid=int(len(a)-1)//2
print("sum of value:",s)
print("avg",avg)
print("mid",a[mid])
'''
#sum of digit:
#method 1 
'''
a='a1b2c3'
sum=0
for i in a:
    if i.isdigit():
        sum=sum+int(i)
print(sum)
''' 
#method 2
'''
def sum(a):
    sum=0
    for i in a:
        if i.isdigit():
            sum=sum+int(i)
    return sum
a='a1b2c3'
b=sum(a)
print(b)
'''
#add two number without using arthematic operator:
'''
a=int(input("enter he number"))
b=int(input("enter the number"))
print(a.__add__(b))
'''
#use lambda function to add two number:
'''
add=lambda x,y:x+y
print(add(2,3))
'''
#use lambda function to multiple three number:
'''
multiple=lambda x,y,z:x*y*z
print(multiple(1,2,3))
'''
#combination of list:
'''
a=[1,2,3]
b=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if (i!=j):
            b.append((a[i],a[j]))
            print(b)
print()
'''

#method 2 using module:
'''
from itertools import permutations
perm=permutations([1,2,3])
for i in list(perm):
    print(list(i))
print()
'''
#combination of set:
'''
a={1,2,3}
b=set()
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            b.add((i,j))
            print(b)
print()
'''
#method 2 using module:
'''
from itertools import permutations
perm=permutations({1,2,3})
for i in set(perm):
    print(set(i))
'''
#most freqent element in array-[securden interview]
'''
def mf(a,n):
    max_count=0
    max_frequency=0
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if a[i]==a[j]:
                count+=1
        if count>max_count:
            max_count=count
            max_frequency=a[i]
    return max_frequency
a=[1,8,8,4,5,5,5,5,5,5,5]
n=len(a)
print(mf(a,n))
'''
#count freqency of the char or No of occurenc of th char:
#method 1
'''
a="abccdeff"
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print("freqency of the char")
print(d)

'''
#method 2:
'''
name=input("enter the name")
from collections import Counter
data=Counter(name)
print("freqency of the char",name,'is')
print(str(data))
'''
#putting zero 0 last
'''
a=[1,2,0,0,3,4,0,5,0]
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
for j in b:
    c.append(j)
print(c)
'''
#putting negative number to last
'''
a=[1,-1,2,-2,3,-3,-4,4,5]
b=[]
c=[]
for i in a:
    if i<0:
        b.append(i)
    else:
        c.append(i)
for j in b:
    c.append(j)
print(c)
'''
#putting zero at Middle:
'''
a="12345"
for i in a:
    i=i+"0"
    print(i,end="")
'''
#remove space  on the given string:
#method 1:
'''
a="hey hi i am jubair "
x=a.replace(" ","")
y=len(x)
print(x)
print(y)
'''
#method 2:
'''
a="hey hi i am jubair"
b=0
for i in a:
    if i in " ":
       print("",end="")
       continue
    #else:
        #b=b+1
    b=b+1    
print(b)
'''
#method
'''
a="hey hi i am jubair"
b=0
for i in a:
    if i in " ":
        print("",end="")
    else:
        print(i,end="")
print('\n')
for i in a:
    if i in a:
        b=b+1
print(b)
'''
'''
#find minmu and maximum value of an array:
a=[2,3,44,100,1000,33,105,1,70]
b=a[0]
c=a[0]
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
    if a[i]<c:
        c=a[i]
print("max number",str(b))
print("min number",str(c))
'''
#find second largest number in the array:
'''
a=[1,2,3,4,5,6,6,6,7,7,8]
b=a[0]
c=a[0]
d=a[0]
e=a[0]
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
print("first largest number :", str(b))
for i in range(len(a)):
    if a[i]>c and a[i]!=b:
       c=a[i]
    if a[i]<d:
        d=a[i]
print("second largest number :",str(c))
print("first minimum number:",str(d))
'''
#method 2 simple way:
'''
for i in range(len(a)-1,-1,-1):
    if a[i]!=a[i-1]:
        print(a[i-1])
        break
'''     
#swap the number
'''
a=1
b=2
print("before swapping")
print(a)
print(b)
a,b=b,a
print("after swapping")
print(a)
print(b)
'''
#swap the number using third variable:
'''
a=1
b=2
print("before swapping")
print(a)
print(b)
temp=a
a=b
b=temp
print("after swapping")
print(a)
print(b)
print(temp)
'''
#vowel count in the name:
'''
a=input("enter the name :")
vowel=0
consonent=0
for i in a:
    if i in "aeiou":
        vowel=vowel+1
    else:
        consonent=consonent+1
print(vowel)
print(consonent)
'''
#remove vowel in the given string:
'''
a=input("enter the string :")
for i in a:
    if i in "aeiou":
        print("",end="")
    else:
        print(i,end="")
'''
#leap year or not:
'''
n=int(input("enter the year: "))
if n%4==0:
    print("leap year")
else:
    prin("non leap year")
'''
#sort the given using BUBBLE SORT in ascending order:
'''
def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:             #> asc order , < desc order
                t=a[j]                        
                a[j]=a[j+1]
                a[j+1]=t
    return a
a=[1,4,5,2,3,7,8]
print(bubblesort(a))
'''
#binary number or not:
'''
num=int(input("enter the number :"))
while 0<num:
    i=num%10
    if i!=0 and i!=1:
        print(" this is not binary number ")
    num=num//10
if num<=1:
   print("this binary number")
'''
#perfect number or not:
'''
num=int(input("enter the number"))          #perfect number-6,28,496,8128
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("this is perfect number")
else:
    print("this is not perfec number")
'''
#ambical pair or not:
'''
a=int(input("Enter the number :"))
a1=[]
b=int(input("Ener the number :"))        #ambical pair numbers-(220,284),(1184,1210),(2620,2924)
b1=[]
for i in range(1,a):
    if a%i==0:
        a1.append(i)
for j in range(1,b):
    if b%j==0:
        b1.append(j)
c=sum(a1)
d=sum(b1)
if a==d and b==c:
    print("ambical pair")
else:
    print("not ambical pair")
'''
#angaram or not:
'''
a=input("Enter the name :")
b=input("Enter teh name :")
if sorted(a)==sorted(b):
    print("this is angaram")
else:
    print("this not anagram")
'''
#amstrong number or not:
'''
num=int(input("enter the number"))
i=num
sum=0
order=len(str(num))          #amstrong number-0,1,153,370,371,407
while i!=0:
    digit=i%10
    sum=sum+digit**order
    i=i//10
if sum==num:
    print(num,"this is amstrong number")
else:
    print(num,"this is not amstrong number")
'''
#check amstrong number or not:
'''
for i in range(100,1001):
    num=i
    sum=0
    order=len(str(num))
    while i!=0:
        digit=i%10
        sum=sum+digit**order
        i=i//10
    if num==sum:
       print(num)
'''
#check palindrom or not:
#method 1:
'''
def isplaindrom(s):
    return s==s[::-1]
s=input("enter the string : ")
reverse=isplaindrom(s)
if reverse:
    print("this is palindrom")
else:
    print("this is no palindrom")
'''    
#method 2 using if class :
'''
n=input("Enter the sring : ")
reverse=n[::-1]
if reverse==n:
    print("this is palindrom")
else:
    print("this is not palindrom ")
'''
#given number is palindrom or not:  [easy method]:
'''
s=int(input("enter the number :"))
n=str(s)
rev=n[::-1]
if rev==n:
    print("Palindrom")
else:
    print("Not Palindrom")
'''
#check given number is palindrom or not:
'''
num=int(input("Enter the number : "))
i=num
rev=0
while 0<i:
    digit=i%10
    rev=rev*10+digit
    i=i//10
if num==rev:
    print("this  is palindrom number")
else:
    print("this not palindrom number")
'''    
    
#use recursion function check whether  it is prime or not:
'''
def checkprime(i,num):
    if num==i:
        return 0                   #prime number-2,3,5,7,11,13,17,19,23
    if num%i==0:
        return 1
    else:
        return checkprime(i+1,num)
num=int(input("Enter the number"))
if (checkprime(2,num)==0):
    print("prime number")
else:
    print("not prime number")
'''
#using for loop to check prime or no:
'''
num=int(input("Enter the number"))
for i in range(2,num):
    if num%i==0:
        print(" Not prime number")
        break
else:
    print("prime number")
'''
#find the inerval of the given prime number:
'''
num=int(input("Enter the number"))
for i in range(2,num):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
#using recursion funcion  print fibonnoci series:
#method 1:
'''
def fib(n):
    if n<=1:
        return n
  else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the number : "))
for i in range(n):
    print(fib(i))
'''
#use for loop o print fibonnoci series:
#method 2:
'''
num=int(input("Enter he number : "))
a=0
b=1
s=0
for i in range(num):
    print(s)
    s=a+b
    b=a
    a=s
'''
#use recursion function to print factorial number :
#method 1:
'''
def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter he number :  "))
a=fact(num)
print(a)
'''
#using for loop o print factorial number
#method 2:
'''
num=int(input("enter the number : "))
factorial =1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial)
'''
#user input in matrix 3x3:
'''
r=int(input("Enter the row :"))
c=int(input("Enter the column :"))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"Enter a[{i}][{j}] "))
        t.append(val)
    a.append(t)
b=[]
r=int(input("Enter the row :"))
c=int(input("Enter the column :"))
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"Enter a[{i}][{j}] "))
        t.append(val)
    b.append(t)
sum=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]+b[i][j]
        t.append(val)
    sum.append(t)
print(sum)
'''
#rotate matrix in 90 degree 3x3:
'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
#for k in b:             #used for matrix transpose
    #print(k)
for k in b:
    print(k[::-1])      #matrix rotation right side 90-degree k[::-1],matrix rotation left side k[::1] 90-degree
'''

#add matrix:
'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for k in c:
    print(k)
'''
#matrix add using function :
'''
def mat(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            c[i][j]=a[i][j]+b[i][j]
    for k in c:
        print(k)
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
d=mat(a,b)
print(d)
'''
#matrix multplication:
'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]*b[i][j]
for k in c:
    print(k)
                   
'''
#matrix transpose using 2x2:
'''
a=[[1,2],[3,4]]
b=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for k in b:                             #matrix transpose
    print(k)
for k in b:
    print(k[::-1])                      #matrix rotation
'''    
#linear search:
#method 1:
'''
a=[1,2,3,4,5,6,7,8]
key=int(input("enter the search key "))
for i in range(len(a)):
    if a[i]==key:
        print("key is found in the postion :",i)
        break
else:
    print("key is not found")
'''
#method 2:
'''
n=int(input("enter the inerval :"))
a=[]
for i in range(n):
    b=int(input("Enter :"))
    a.append(b)
print(a)
key=int(input("enter the key postion :  "))
for j in range(len(a)):
    if a[j]==key:
        print("key is found and postion is :",j)
        break
else:
   print("Key is not found")
'''
#linear search using sort method:
'''
n=int(input("enter the interval :"))
a=[]
for i in range(n):
    b=int(input("enter :"))
    a.append(b)
a.sort()
print(a)
key=int(input("enter the key :"))
for j in range(len(a)):
    if a[j]==key:
        print("key found in the postion",j)
        break
else:
    print("key is not found")
'''
#method 3 using function:
'''
def search(key,list):
    for i in range(len(a)):
        if a[i]==key:
            print("key is found in the postion ",i)
            break
    else:
        print("key is not found in the postion")
a=[1,2,3,4,5,6,7]
print(a)
key=int(input("enter the key : "))
search(key,list)
'''
#method 4 using class [oops]:
'''
class linear:
    def __init__(self,a,key):
        self.a=a
        self.key=key
    def search(self):
        for i in range(len(a)):
            if a[i]==key:
                print("key is found",i)
                break
        else:
            print("key is not found")
a=[1,2,3,4,5]
print(a)
key=int(input("enter the key "))
c=linear(key,a)
c.search()
'''
#binary search easy method:
'''
a=[]
n=int(input("enter the value :"))
for i in range(n):
    b=int(input("enter The List number :"))
    a.append(b)
a=sorted(a)
print(a)
k=int(input("Enter the key postion :"))
def binary(num,array,low,high):
    if high<low:
        return -1
    mid=(low+high)//2
    if num==array[mid]:
        return mid
    elif num<array[mid]:
        return binary(k,a,low,mid-1)
    else:
        return binary(k,a,mid+1,high)
def search(k,a):
    return binary(k,a,0,len(a)-1)
b=search(k,a)
if b<0:
    print("key is not found")
else:
    print("key is found in the postion",b+1) 
'''
#binary search:
'''
def binary(n,l,h,x):
    if h>=1:
        m=l+(h-1)//2
        if n[m]==x:
            return m
        elif n[m]>x:
            return binary (n,l,m-1,x)
        elif n[m]<x:
            return binary (n,m+1,h,x)
    else:
        return -1
n=[1,2,3,4,5,6]
x=5
r=binary(n,0,len(n)-1,x)
if r!=1:
   print("key is found in the postion : ",r)
else:
    print("key is not found in the postion")
'''
#three  types binary  tree traversal :
#preorder traversal:
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("binary tree preorder traversal")
preorder(root)
print()
'''
#inorder traversal:
'''
class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("Binary tree inorder traversal ")
inorder(root)
print()
'''
#postorder traversal:
'''
class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def postorder(root):
    if root:
       postorder(root.left)
       postorder(root.right)
       print(root.val)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
postorder(root)
print("binaary ree postorder traversal")
print()
'''
#basic calci program without constructor:
'''
class calci:
    def add (self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
c=calci()
print(c.add(1,2))
print(c.sub(3,2))
'''
#method 2 with __init__  constructor
'''
class calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add (self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
c=calci(2,3)
print(c.add())
print(c.sub())
'''    
#calci program using class:
'''
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
class calci:
      def __init__ (self,a,b):
          self.a=a
          self.b=b
      def add(self):
          return self.a+self.b
      def sub(self):
          return self.a-self.b
print("1.add")
print("2.sub")
c=calci(a,b)
choice=int(input("Enter the choice: "))
if choice==1:
    print(c.add())
elif choice==2:
    print(c.sub())
else:
    print("ERROR")
'''
#---------------------------------------------------------------------
#oops concept:
#abstraction:
#REALTIME Example- TV remote [when we use the tv remote to increase
#the volume we don't know how pressing a key increase the volume of the TV
#we only konw to press the + button to increase the volume :exactly abstraction wrks
'''
from abc import ABC
class college(ABC):
    def type(self):
        pass
class Mcollege(college):
    def type(self):
        print("i am medical college student")
class Ecollege(college):
    def type(self):
        print("i am enineering college student")
class Acollege(college):
    def type(self):
        print("i am arts college student")
a=Mcollege()
b=Ecollege()
c=Acollege()
a.type()
b.type()
c.type()
'''
#encapsulation:
#REALTIME Example- Driving wheel and calci is encapsulation
#bcz the process of Rotating wheel from you as same like calci(calculator)  
'''
class calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
c=calci(1,5)
print(c.add())
print(c.sub())
'''
#polymorphism
#REALTIME Example -a person at the same time can have different characterstics
#like man at the same time  is a father,a husband, an employee
'''
class record1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def type(self):
        print(self.name,self.age)
class record2:
    def __init__(self,rollno,dept):
        self.rollno=rollno
        self.dept=dept
    def type(self):
        print(self.rollno,self.dept)
r1=record1("jubair","23")
r2=record2("1234","IT")
r1.type()
r2.type()
'''
#two typs of polymorphism:
#     1.Method overloading
#     2.Method overriding

#Method Overloading:
# Method overloading allows multiple methods in the same class to have the same name but different parameters.
'''
class calci:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
c=calci()
print(c.sum(1,2,3))
'''
#Method Overiding:
# Method overriding allows a parent class and a child class to have methods with the same name and same parameters
'''
class father:
    def mob(self):
        print("Nokia mobile")
class me(father):
    def mob(self):
        print("Redmi Mobile")

a=me()
a.mob()
'''
#inheritance:
#REALTIME Example we are humans we inherit certain properties from
#the class "human" such as ablit to speak ,breath,eat,drink etc..., 
'''
class gfather:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def gen1(self):
        print(self.name,self.age)
class myfather(gfather):
    def __init__(self,name,age,rollno,dept):
        gfather.__init__(self,name,age)
        self.rollno=rollno
        self.dept=dept
    def gen2(self):
        print(self.rollno,self.dept)
class myson(myfather):
    def gen3(self):
        print(self.name,self.dept)
a=gfather("sugan","66")
b=myfather("chinu","45","1234","IT")
c=myson("jubair","23","1234","IT")
a.gen1()
b.gen2()
c.gen3()
'''
#singel inheritance:
'''
class father:
    def props(self):
        print("land,car,bankbalance")
class son(father):
        "i am 24"
        pass
a=son()
a.props()
'''
#multi inhertiance:
'''
class father:
    def props(self):
        print("land ,car, house")
class fatherbrother:
    def prop(self):
        print("saving,insurance,prop")
class son(father,fatherbrother):
    "i am 24"
    pass
a=son()
a.props()
a.prop()
'''
#multi-level inheriance:
'''
class gf:
    def gen1(self):
        print("3rd gen")
        pass
class f(gf):
    def gen2(self):
        print("2nd gen")
        pass
class me(f):
    def gen3(self):
        print("1rd gen")
        pass
a=me()
a.gen3()
a.gen2()
a.gen1()
'''
#hierarchical inheritance:
'''
class kasim:
    def props(self):
        print("land,saving,insurance ,house")
class salman(kasim):
    "i am 27"
    pass
class jubair(kasim):
    "i am 24"
    pass

a=salman()
b=jubair()
a.props()
b.props()

'''
#add two list
'''
a=[1,2,3,4]
b=[5,6,7,8]
for i in b:
    a.append(i)
print(a)
'''
#combination of string
'''
a="SLA"
b=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            b.append((a[i],a[j]))
            print(b)
print()
'''
'''

from itertools import permutations
perm=permutations("sla")
for i in perm:
    print(i)
'''
# set difference without build in function:
'''
a=[1,3,5,7,9,10]
b=[3,5,7]
q={i for i in a if i not in b}
print(q)
'''
#                   <-----------------------------SUM OF SERIES [Arthematic series]------------------------------>
#sum of series 1,2,3,4,...N:
'''
sum=0
a=1                      #starting value
n=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a
    a+=1                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of series 10+9+8...N:
'''
sum=0
a=10                      #starting value
n=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a
    a-=1                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of series 9+13+17...N
'''
sum=0
a=9                     #starting value
n=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a
    a+=4                #differnce value in both number
print("sum of series: ",sum)
'''
#sum of series 2+4+6+8...20
'''
sum=0
a=2                     #starting value
n=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a
    a+=2               #differnce value in both number2,4,6
print("sum of series: ",sum)
'''
#sum of series 1+3+5+7...N
'''
sum=0
a=1                    #starting value
n=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a
    a+=2                #differnce value in both number2,4,6
print("sum of series: ",sum)
'''
#--------------------------------------------------------------------------------------------------------------------
#sum of series x1+x2+x3+x4...N:
'''
sum=0
a=1                      #starting value
n=int(input("enter"))
x=int(input("enter"))
for i in range(1,n+1):
    sum=sum+x**a
    a+=1                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of sries 9!/x+13!/x+17!/x....N
'''
import math as m
sum=0
a=9                      #starting value
n=int(input("enter"))
x=int(input("enter"))
for i in range(1,n+1):
    sum=sum+m.factorial(a)/x
    a+=4                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of sries 2^x+4^x+6^x+8^x....N
'''
sum=0
a=2                      #starting value
n=int(input("enter"))    #n=10
x=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a**x
    a+=1                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of series 1^3/x+3^3/x+5^3/x+7^3/x...N
'''
sum=0
a=1                      #starting value
n=int(input("enter"))    #n
x=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a**3/x
    a+=2                 #differnce value in both number
print("sum of series: ",sum)
'''
#sum of series 2/10+4/9+6/8+8/7+...20/1
'''
sum=0
a=2                      #numrator value
d=10                      #denaminator value
n=int(input("enter"))    #n=10
x=int(input("enter"))
for i in range(1,n+1):
    sum=sum+a/d
    a+=2                 #differnce value in both number
    d-=1
print("sum of series: ",sum)
'''
#sum of series x/2+x/4+x/8+x/16+...N
'''
sum=0
k=2
x=int(input("enter :"))
n=int(input("enter :"))
for i in range(1,n+1):
    sum=sum+x/k
    k=k*2
print(sum)
'''
#sum of series 2-6+18-54+...N
'''
sum=0
k=2
x=int(input("enter :"))
n=int(input("enter :"))
for i in range(1,n+1):
    if i%2==0:
       sum=sum+k
    else:
       sum=sum-k
    k=k*3
print(sum)
'''
#sum of series x+2/10+x+4/30+x+6/90+...N:
'''
sum=0
a=2
k=10
x=int(input("enter :"))
n=int(input("enter :"))
for i in range(1,n+1):
       sum=sum+(x+a)/k
       a=a+2
       k=k*3
print(sum)
'''
#sum of series input 1+3/4+6/9+10/15+..
'''
sum=0
n=int(input("enter"))
for i in range(0,n):
    a=int(input("enter"))
    b=int(input("enter"))
    sum=sum+a/b
print(sum) 
'''
#                  <----------------------------SUM OF SERIES[gementric seris]------------------------------------>
#sum of series 2+4+8+16...N
'''
sum=0
k=2
for i in range(1,n+1):
    sum=sum+k
    k=k*2
print(sum)
'''
#sum of series 2+8+16+54...N
'''
sum=0
k=2
for i in range(1,n+1):
    sum=sum+k
    k=k*3
print(sum)
'''
#sum of series 5+25+125+...N
'''
sum=0
k=2
for i in range(1,n+1):
    sum=sum+k
    k=k*5
print(sum)
'''
#sum of series 10+30+90+270+...N
'''
sum=0
k=10
for i in range(1,n+1):
    sum=sum+k
    k=k*3
print(sum)
'''

#add two number without build in function:
'''
num1=2
num2=5
pro=0
for i in range(1,num2+1):
    pro=pro+num1
print(pro)
'''
#solvrines question:
#3x3 user input matrix:
'''
r=int(input("Enter the row 1st matrix:"))
c=int(input("Enter the column 1st matrix:"))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"Enter a[{i}][{j}] :"))
        t.append(val)
    a.append(t)
r=int(input("Enter the row 2nd matrix:"))
c=int(input("Enter the column 2nd matrix:"))
b=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"Enter a b[{i}][{j}] :"))
        t.append(val)
    b.append(t)
sum=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]+b[i][j]
        t.append(val)
    sum.append(t)
print(sum)
'''
#user input string remove duplicate:
'''
a=input("Enter the string"))
b=input("enter empty string b "))
c=input("enter empty string c "))
for i in a:
    if i not in b:
        b=b+i
    else:
        c=c+i
print(b)
print(c)
'''

#user input a pararaph and remove duplicate :
'''
a="""hey hi i am jubair
hey hi """
b=a.split()
for i in range(len(b)):
    for j in range(len(b)-1,i,-1):
        if b[i]==b[j]:
            print(b[j],end="\n")
            
'''
#method 2:
'''
a=""" we are the batch met of
pyhon and we are"""
c=''
d=''
b=a.split()
for i in b:
    if i not in c:
        c=c+i
    else:
        d=d+i
print("Orignal:",c)
print("Duplicate :",d)
#usr input freqncy of the list:
'''
#no.of occurnece of the list
'''
n=int(input("enter the interval :"))
a=[]
for i in range(n):
    b=int(input("enter"))
    a.append(b)
print(a)
d=dict()
for i in a:
    if  i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
'''
#user input whether given matrix is true or false:
'''
r=int(input("enter a row :"))
c=int(input("enter a colunm:"))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"enter a[{i}][{j}]:"))
        t.append(val)
    a.append(t)
r=int(input("enter a row :"))
c=int(input("enter a colunm:"))
b=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"enter a[{i}][{j}]:"))
        t.append(val)
    b.append(t)
print(a)
print(b)
def jub(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][j]==b[i][j]:
                c=True
            else:
                c=False
    return c
e=jub(a,b)
print(e)
            
'''
'''
n=int(input("enter the intervals : "))
a=[]
for i in range(n):
    b=int(input("enter :"))
    a.append(b)
print(sorted(a))

'''
'''
r=int(input("enter the row :"))
c=int(input("enter the column: "))
a=[]
for i in range(r):
    t=[]
    for j in range(c): 
        v=int(input(f"entr a[{i}][{j}] : "))
        t.append(v)
    a.append(t)
print(a)
'''


# *--star--- pattern program:

#right-angel triangel[increasing triangel]:
'''
n=int(input("enter the interval :"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
'''
#left-angel triange[decreasing triangel]:
'''
n=int(input("Enter the interval :"))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")    
    print()
'''
#reverse-right angel triangle:
'''
n=int(input("enter the interval : "))
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print("*",end="")
    print()
'''
#reverse-left angel triangel:
'''
n=int(input("enter the interval :"))
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()
'''
#hill star pattern:
'''
n=int(input("enter the interval :"))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
'''
#reverse hill star pattern:
'''
n=int(input("enter the interval:"))
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end="")
    for j in range(i,n):
        print('*',end="")
    print()
'''
#diamond star pattern:
'''
n=int(input("enter the interval :"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end="")
    for j in range(i,n):
        print('*',end="")
    print()
'''
'''
n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(chr(p),end="")
    for j in range(i+1):
        print(chr(p),end="")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print(chr(p),end="")
    for j in range(i,n):
        print(chr(p),end="")
    print()

'''
'''
n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p-=1
    print()
'''
'''
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    for j in range(i):
        print("",end="")
    for j in range(n-i):
        print(p,end="")
    p+=1
    print()
'''
'''
n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(' ',end="")
``    for j in range(n-i):
        print(p,end="")
        p-=1
    print()

n=5
p=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p-=1
    print()
'''    
#data strcture program:
#1.subarray with given sum arr=[10,2,-2,-20,-10] sum=-10,arr=[1,4,20,3,10,51] sum=33:
'''
def subarray(a,sum):
    dict={}
    csum=0
    for i in range(len(a)):
        csum=csum+a[i]
        if csum==sum:
            print("subarray start from 0 to",i)
            break
        if csum-sum in dict:
            print("subarray start from",dict[csum-sum]+1,"to",i)
            break
    else:
        dict[csum]=i
        print("No subarray found")
a=[10,2,-2,-20,-10]
sum=-10
subarray(a,sum)
'''
#longest conscutive subseqence
#method 1:
'''
def LongestConseqSubseq(arr, l):
    val = []
    c = 0
    for i in range(l):
        n = 1
        while arr[i] + n in arr:
            c += 1
            n += 1
        val.append(c + 1)
        c = 0
    return max(val)
array = [7, 8, 1, 5, 4, 3]
print("Longest Consecutive Subsequence :", LongestConseqSubseq(array, len(array)))
'''
#method 2 easy:
'''
def lcs(num):
    a=set(num)
    b=0
    for i in num:
        if i in a:
            a.remove(i)
            c=i-1         #next number
            d=i+1         #previous number   
            while c in a:
                a.remove(c)
                c-=1      #c=c-1
            while d in a:
                a.remove(d)
                d+=1      #d=d+1
            b=max(b,d-c-1)
    return b
num=[100,4,200,1,3,2]
print(lcs(num))
'''
#longest common subsequence:
'''
def sub(t1,t2):
    m=len(t1)
    n=len(t2)
    lcs=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(0,m+1):
        for j in range(0,n+1):
            if (t1[i-1]==t2[j-2]):
                lcs[i][j]=1+lcs[i-1][j-1]
            else:
                lcs[i][j]=max(lcs[i][j-1],lcs[i-1][j])
    return lcs [m][n]
t1="abcdefgh"
t2="bcdef"
print("longest common subsequenc :",sub(t1,t2))              
'''
#rearrange altrnate positive and negative number:
'''
def rearrange(arr,n):
    i=-1
    for j in range(n):
        if (arr[j]<0):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            pos,neg=i+1,0
    while (pos<n and neg<pos and arr[neg]<0):
        arr[neg],arr[pos]=arr[pos],arr[neg]
        pos+=1
        neg+=2
def printarray(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
arr=[1,2,3,4,5,-1,-2,-3,-4,-5]
n=len(arr)
rearrange(arr,n)
printarray(arr,n)
'''
#rearrange array in altrnately in maximum and minmum form:
#method 1:
'''
def rearrange(a,n):
    max_index=n-1
    min_index=0
    max_element=a[n-1]+1
    for i in range(0,n):
        if i%2==0:
            a[i]+=((a[max_index]%max_element)*max_element)
            max_index-=1
        else:
            a[i]+=((a[min_index]%max_element)*max_element)
            min_index+=1
    for i in range(0,n):
        a[i]=a[i]/max_element
a=[1,2,3,4,5,6]
n=len(a)
rearrange(a,n)
for i in range(0,n):
    print(int(a[i]),end=" ")
'''
#method 2:
'''
def rearrange(a,n):
    max_element=a[n-1]
    min_element=a[0]
    for i in range(n):
        if i%2==0:
            a[i]=max_element
            max_element-=1
        else:
            a[i]=min_element
            min_element+=1
a=[1,2,3,4,5,6]
n=len(a)
rearrange(a,n)
for i in range(n):
    print(a[i],end=" ")
'''
#longest palindrom in the string:
'''
def longestpalindrom(s):
    counts=dict()
    for i in s:
        counts[i]=counts.get(i,0)+1
        result,oddfound=0,False
    for  i in counts.values():
        if i%2==0:
            result+=i
        else:
            oddfound=True
            result+=i-1
    if oddfound:
        result+=1
    return result
s="abccccdd"
print("longest palindrom in the string :",longestpalindrom(s))
'''
#longest palindrom in a string :
'''
def longestPalindrome(s):
    length=len(s)
    index=-1
    maxlength=0                        
    for i in range(length):# looping over the string for substrings
        for j in range(i,length):
	    ispalindrome=1
	    for k in range(0,((j-i)//2)+1):# checking if string is a palindrome
		if s[i+k]!=s[j-k]:
		    ispalindrome=0
	    if ispalindrome != 0 and j-i+1>maxlength:# if the string is palindrome update maximum length 
		index=i
		maxlength=j-i+1                                            
    return s[index:index+maxlength]# return the substring from updated index till length maxlength
s= "aaaabbaa"
print(longestPalindrome(s))
'''
# most frequent element:
'''
def mf(a,n):
    maxc=0
    maxf=0
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if a[i]==a[j]:
                count+=1
        if count>maxc:
            maxc=count
            maxf=a[i]
    return maxf
a=[1,2,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5,5]
n=len(a)
print("most frquent" , mf(a,n))
'''
#spiral matrix traverse    4x4
'''
def spiralmatrix(a,i,j,m,n):                    
    if (i>=m or j>=n):                                            # If i or j lies outside the matrix
        return a[i][j]
    for p in range(i,n):                                          # Print First Row
        print(a[i][p],end=" ")
    for p in range(i+1,m):                                        # Print Last Column
        print(a[p][n-1],end=" ")
    if((m-1)!= i):                                                # Print Last Row, if Last and  # First Row are not same
        for p in range(n-2,j-1,-1):
            print(a[m-1][p],end=" ")
    if((n-1)!=j):                                                 # Print First Column, if Last and ,# First Column are not same
        for p in range(m-2,i,-1):
            print(a[p][j],end=" ")
    spiralmatrix(a,i+1,j+1,m-1,n-1)
R=4
C=4
a=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
spiralmatrix(a,0,0,R,C)                                          # Function Call
'''
#spiral-traverse matrix program it work in all formate:
'''
def spirallyTraverse(matrix,r,c): 
    row = 0 
    col = 0
    output = []
    while (row<r and col<c):                                          
        for i in range(col,c) :                         #storing the elements of 1st row from the remaining rows, in a list.
            output.append(matrix[row][i])      
        row+=1                                        
        for i in range(row,r):                          #storing elements of last column from remaining columns, in list.
            output.append(matrix[i][c-1]) 
        c-=1                                        
        if(row<r):                                      #storing the elements of last row from remaining rows, in a list.
            for i in range(c-1,(col-1),-1) : 
                output.append(matrix[r-1][i]) 
            r-=1                                          
        if(col<c):                                       #storing elements of 1st column from remaining columns, in list. 
            for i in range(r-1,row-1,-1) : 
                output.append(matrix[i][col])   
            col += 1                                                      
    return output                                       #returning the list.
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r=4
c=4
print(spirallyTraverse(matrix,r,c)) 
'''
#kadaen's algorithm[maximum sum of subarray]:
'''
def maxsubarray(a):
    maxsum=a[0]
    currsum=0
    for i in a:
        if currsum<0:
            currsum=0
        currsum+=i
        maxsum=max(maxsum,currsum)
    return maxsum
a=[-1,-2,-3,-4]
print("max subarray of sum is" , maxsubarray(a))
'''
#prenthesis checker program :
'''
def parenthesis_checker(a):
    c=[]                      #stack
    b={ '(': ')', '{': '}','[': ']' }
    for i in a:
        if i in ["(", "{", "["]:
            c.append(b[i])    # push the closing parenthesis in the c
        elif not c:           # If the current character is not opening ,#, then it is a closing one.,# and the c cannot be empty at this point
            return False
        elif i != c.pop():
            return False
    if c:                    # see if the c has any values
        return False
    return True
a = "{[()]}"
if parenthesis_checker(a):
    print("expression is balanced")
else:
    print("expression is not balanced")
'''
#minmum number of jumps[jump game -1]:  only for true or false condition program
'''
def canJump(a):
        b=a[0]
        for i in range(0,len(a)-1):
            b=max(b-1,a[i])
            if b==0:
                return False
        return True
a=[2,3,1,1,4]
print(canJump(a))
'''
#minmum number of jumps[jump game-2]:
'''
def jump(a):
    jumps=curEnd=curFarthest=0
    for i in range(len(a)-1):
        curFarthest=max(curFarthest,i+a[i])
        if i==curEnd:
            jumps+=1
            curEnd=curFarthest
    return jumps
a=[1,3,5,8,9,2,6,7,6,8,9]            #input- [2, 3, 1, 1, 4] o/p=2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] o/p-10
print(jump(a))
'''
#kth smallest element program:
'''
def kthsmallest(a,n,k):
    a.sort()
    return a[k-1]
a=[7,10,4,20,15]
n=len(a)
k=4
print("kth smallest element",kthsmallest(a,n,k))
'''

