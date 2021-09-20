#!/usr/bin/env python
# coding: utf-8

# In[36]:


print('Hello World')


# In[ ]:





# In[8]:


num1=input('Enter a number: ')
num2=input('Enter a number: ')
add=int(num1)+int(num2)
print('The sum of {0} and {1} is {2}'.format(num1,num2,add))


# In[12]:


import cmath
a= float(input('Enter a value: '))
b= float(input('Enter a value: '))
c= float(input('Enter a value: '))

d= ((b**2)-(4*a*c))

sol1= (-b-cmath.sqrt(d))/(2*a)
sol2= (-b+cmath.sqrt(d))/(2*a)

print('The solution of this quadratic equation is {0} and {1}'.format(sol1,sol2))


# In[13]:


P= int(input('Enter a value: '))
Q= int(input('Enter a value: '))

P=P^Q
Q=P^Q
P=P^Q

print('the value of P is',P,'The value of Q is',Q)


# In[17]:


import random 
n=int(random.random())
print(n)


# In[22]:


import random 
n=random.randint(0,50)
print(n)
if (n%2==0):
    print('heads')
else: 
    print('tails')


# In[33]:


c=float(input('Enter temperature in Celsius: '))
f= (c*9/5)+32
print(f)


# In[27]:


X=[[1,2,3],[4,5,6],[7,8,9]]
Y=[[10,11,12],[13,14,15],[16,17,18]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(X)):
        result[i][j]=X[i][j]+Y[i][j]
      
for r in result:
    print(r)


# In[30]:


A=[[5,4,3],
   [2,4,6],
   [4,7,9]]
B=[[3,2,4],
   [4,3,6],
   [2,7,5]]
C=[[0,0,0],
  [0,0,0],
  [0,0,0]]

for i in range(len(C)):
    for j in range(len(C[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]
            
for r in C:
    print(r)


# In[31]:


A=[[5,4,3],
   [2,4,6],
   [4,7,9],
   [1,2,3]]
C=[[0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]]
for a in range(len(A)):
    for b in range(len(A[0])):
        C[b][a]=A[a][b]
        
for r in C:
    print(r)


# In[32]:


inside=['g1','g2','g1','g2']
outside=[1,2,3,1]
output=list(zip(outside,inside))
print(output)


# In[ ]:





# In[ ]:




