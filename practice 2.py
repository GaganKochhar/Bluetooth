#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Take string input

my_str= input('Enter a string: ')

#Split the string into words

words= my_str.split()

#Sort the words

words.sort()

for word in words:
    print(word)


# In[4]:


#Remove Punctuations

punc=  '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
my_str= input('Enter a string: ')
no_punc=''
for char in my_str:
    if char not in punc:
        no_punc=no_punc+char
        
print(no_punc)        


# In[8]:


#Check if an input number is positive, negative or equal to 0

def NumberCheck(a):
    if (a>0):
        print('Number is Positive.')
    elif (a==0):
        print('Number is equal to 0')
    else:
        print('Number is Negative.')
        
a=float(input('Enter a number: '))
NumberCheck(a)


# In[10]:


def OddEven(a):
    if (a%2==0):
        print('Even')
    else:
        print('Odd')

a=float(input('Enter a number: '))
OddEven(a)


# In[12]:


def LeapYear(a):
    if((a%400==0)or(a%100!=0)and(a%4==0)):
        print('It is a leap year!')
    else:
        print('It is not a leap year!')
    
a=int(input('Enter a year: '))
LeapYear(a)


# In[18]:


#Checking if a number is Prime

def PrimeNo(a):
    if a>1:
        for i in range(2,int(a/2)+1):
            if (a%i==0):
                print('Not Prime')
                break
        else: 
            print('Prime')
    else:
        print('Not Prime Not Composite')
        
a=int(input('Enter a number: '))
PrimeNo(a)


# In[25]:


#Finding Prime numbers from a range of numbers.

low=int(input('Enter the lower limit: '))
up=int(input('Enter the upper limit: '))

for i in range(low,up+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                    print(i)

            


# In[37]:


#finding factorial using normal method

num1=int(input('Enter a Number: '))
result=1
if num1>0:
    for i in range(1,num1+1):
        result=result*i
    print('The factorial of {0} is {1}'.format(num1,result))
elif(num1==0):
    print('Factorial is 1')
else:
    print('Invalid Input')


# In[43]:


#finding factorial using recursive method

def fac(n):
    return 1 if (n==0 or n==1) else n*fac(n-1);

n=int(input('Enter a number: '))
print('Factorial of n is ',)
fac(n)


# In[45]:


#Finding factorial using built-in functions

import math
def fact(n):
    return(math.factorial(n));
n=int(input('enter a number: '))
f=fact(n)
print('Factorial of',n,'is',f)
    


# In[49]:


#displaying multiplication table

x=int(input('Enter a number: '))
res=1
for i in range(1,11):
    res=x*i
    print(x,'multiplied by',i,'is equal to',res)
    
    


# 

# In[59]:


#Fibonacci

terms=int(input('Enter number of terms: '))
n1=0
n2=1
count=0
if (terms<=0):
    print('invalid input')
elif(terms==1):
    print(n1)
else:
    while(count<terms):
        print(n1)
    
        n=n1+n2
        n1=n2
        n2=n
        count+=1
        
            
    


# 

# In[65]:


a=int(input('enter a number: '))
temp=a
sum=0
order=len(str(a))
while(temp>0):
    var=temp%10
    cube=var**order
    sum+=cube
    temp//=10
    
if(sum==a):
    print('armstrong number')
else:
    print('not a armstrong number')


# In[ ]:




