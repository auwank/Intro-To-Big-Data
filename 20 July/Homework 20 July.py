#!/usr/bin/env python
# coding: utf-8

# BASIC EXERCISE #1

# In[1]:


type (1)


# In[2]:


type(3.14)


# In[3]:


type ("Big Data!")


# In[4]:


type('Big Data!')


# In[5]:


type (True)


# In[6]:


type (False)


# In[7]:


type ([1,2,"intruder",3])


# BASIC EXERCISE #2

# In[ ]:


for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print ('Fizz')
    elif i%5==0:
        print ('Buzz')
    else:
        print(i)


# In[ ]:





# BASIC EXERCISE #3

# In[35]:


lst = list(range(1,10))


# In[33]:


max(lst)


# In[34]:


min(lst)


# In[46]:


x=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        x=x+i
print (x)


# BASIC EXERCISE #4

# In[6]:


str = input("Enter string to omit vowels: ")
str2 = str.lower()
x=''
for y in str2:
    if y not in 'a,e,i,o,u':
        x = x+y 
print(x)
    


# ADVANCED EXERCISE #1

# In[62]:


import operator
import collections

str = input('Please type the string to count the characters: ')
d={}
d1={}
#lst=[]
#lst2 = []
str2 = str.lower()
for y in sorted (str2):
    if (y not in ' ') and (y not in lst):
        d[y] = str2.count(y)
        sorted_d = sorted (d.items(), key=operator.itemgetter(1),reverse = True)
        
print(d)
print(sorted_d)


# In[ ]:





# ADVANCED EXERCISE #2

# In[27]:


str = input("Write a  sentence to count occurence of each word: ")
str2 = str.lower()
lst = str2.split()
lst2 = []
for x in lst:
    y=0
    y=lst.count(x)
    if x not in lst2:
        lst2.append(x)
        print(f'Count for "{x}" is {y}')
    
    


# In[ ]:





# ADVANCED EXERCISE #3

# In[28]:


str = input("Please enter comma seperated words: ")
str2 = str.lower()
lst = str2.split(',')
lst.sort()
lst


# In[19]:





# REACH EXERCISE #1 - Not Completed

# In[41]:


lst = list(range(1,25,2))
lst2 = list(range(1,20,3))

lst3=lst+lst2
lst3.sort()
lst3
lst4=[]
for i in lst3:
    if i not in lst4:
        lst4.append(i)
print (lst)
print(lst2)
print (lst4)


# REACH EXERCISE #2 - Not Completed

# In[60]:


x=3
y = 9
count=1
int = len(lst)
a=False
b=False

for i in range(x,y-x):
    for j in range(0, 3):
        a= i%lst[j]==0 
        a = a or a
    for j in range(0, 3):
        b= (y-i)%lst[j]==0 
        b = b or b
    if a and b == True:
        break
    print (y)

    
    


# In[ ]:





# In[ ]:





# In[ ]:




