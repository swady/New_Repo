#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World')


# In[3]:


print('hello world')


# In[9]:


# this is an if and else section
#dfjghdkfjhghk

'''
This is a
multiline comment
this is the 3rd line
'''

if (10>9):
    print('This is an if block')
    print('This is a 2nd line')
    print('True')
else:
    print('False')


# In[13]:


x = 5.0


# In[14]:


print(x)


# In[15]:


type(x)


# In[19]:


x = input('Enter you name ')


# In[20]:


print(x)


# In[21]:


type(x)


# In[26]:


x = int(input('Enter you name '))


# In[27]:


print(x)


# In[24]:


type(x)


# In[32]:


import random

print(random.randrange(10,100))


# In[33]:


x = 10


# In[34]:


type(x)


# In[40]:


x = float(x)


# In[36]:


print(x)


# In[37]:


x = str(x)


# In[38]:


print(x)


# In[39]:


x


# In[41]:


x


# In[42]:


x = 'zero'


# In[43]:


x


# In[61]:


x = 'this is a single line string'


# In[46]:


x = '''this is a multiline string and 
this is the second line.
this is the 3rd line.
'''


# In[47]:


print(x)


# In[62]:


x


# In[56]:


x = 'Hello'


# In[57]:


x[0]


# In[59]:


x[-5]


# In[64]:


x[10:16]


# In[66]:


len('this is a single')


# In[69]:


x[-6:]


# In[71]:


b="Hello, World!"


# In[14]:


a = 6
b = 10
if (a>b):
    print('a is greater')
elif(b>a):
    print('b is greater')
else:
    print('Both are same')


# In[6]:


# this is a shorthand method
if a>b:print('a is grater')


# In[9]:


print('A is greater') if a>b else print('B is greater')


# In[12]:


print('A is greater') if a>b else print('B is greater') if b>a else print('Both are same')


# In[15]:


if a>5:
    if a>b:
        print('a is greater than 5 and greater than b')
    else:
        print('a is greater than 5 but less than b')


# In[17]:


if a>5:
    pass


# In[18]:


a = 10
b = 20
c = 30


# In[19]:


if a>b and a>c:
    print('a is greatest number')
elif b>c and b>a:
    print('b is greatest number')
else:
    print('c is the greatest number')


# In[20]:


if a>b or a>c:
    print('a one of the greatest number')
elif b>c or b>a:
    print('b is one of the greatest number')
else:
    print('c is the greatest number')


# In[24]:


i = 0
while i<=6:
    print(i)
    if i == 3:
        break
    i+=1


# In[26]:


i = 0
while i<=6:
    i+=1
    if i == 3:
        continue
    print(i)
else:
    print('All the executions are over')


# In[33]:


fruits = ['apple','banana','cherry','orange','kiwi']


# In[34]:


con = 0
for i in fruits:
    print(i)
    con+=1


# In[35]:


print(con)


# In[37]:


for x in 'apple':
    print(x)


# In[40]:


for i in fruits:
    print(i)
    if i == 'cherry':
        break


# In[42]:


for i in fruits:
    if i == 'cherry':
        continue
    print(i)


# In[44]:


for i in range(10):
    print(i+1)


# In[48]:


for i in range(3,11):
    print(i)


# In[49]:


for i in range(1,11):
    print(i)


# In[55]:


for i in range(2,11,2):
    print(i)
else:
    print('loop ended')


# In[59]:


x = ['apple','mango','banana']
y = ['red','green','yellow']
for i in x:
    for j in y:
        pass


# In[4]:


x = ['apple', 'mango','banana','mango']


# In[2]:


type(x)


# In[5]:


print(x)


# In[6]:


x[0]


# In[7]:


x[-1]


# In[9]:


x[:3]


# In[10]:


for i in x:
    print(i)


# In[11]:


x.append('orange')


# In[12]:


x


# In[14]:


x.insert(3,'Kiwi')


# In[15]:


x


# In[16]:


x.remove('orange')


# In[17]:


x


# In[18]:


x.remove('mango')


# In[19]:


x


# In[20]:


tup = ('apple','mango','banana')


# In[21]:


type(tup)


# In[22]:


print(tup)


# In[23]:


tup[0]


# In[24]:


tup[-1]


# In[25]:


tup[1:3]


# In[26]:


lis = list(tup)


# In[27]:


lis


# In[28]:


lis.insert(1,'kiwi')


# In[29]:


lis


# In[30]:


tup = tuple(lis)


# In[31]:


tup


# In[34]:


tup = ('apple',)


# In[35]:


type(tup)


# In[36]:


del tup


# In[38]:


t1 = ('apple','mango')


# In[39]:


t2 = (1,2,5,34)


# In[40]:


t3 = t1+t2


# In[42]:


type(t3)


# In[44]:


x = ('apple', 'mango', 'banana', 'Kiwi', 'mango', 'orange')


# In[45]:


print(x)


# In[48]:


x.count('apple')


# In[49]:


x.index('mango')


# In[57]:


x = {'apple', 'mango', 'banana', 'Kiwi', 'mango', 'orange'}


# In[51]:


type(x)


# In[58]:


print(x)


# In[59]:


for i in x:
    print(i)


# In[60]:


x.add('lime')


# In[61]:


x


# In[62]:


y = {1,3,4,5}


# In[63]:


z = x.union(y)


# In[66]:


print(z)


# In[69]:


car = {"brand":"Ford","model":"Mustang","year":1964}


# In[70]:


type(car)


# In[71]:


print(car)


# In[72]:


car['brand']


# In[73]:


car.get('brand')


# In[74]:


car['year'] = 2020


# In[75]:


print(car)


# In[77]:


for i in car:
    print(car[i])


# In[78]:


for i in car:
    print(car.get(i))


# In[79]:


for x,y in car.items():
    print(x,y)


# In[80]:


car['color'] = 'red'


# In[81]:


print(car)


# In[82]:


del car['year']


# In[83]:


car


# In[84]:


car


# In[85]:


car2 = car


# In[86]:


car2


# In[87]:


car2['year'] = 2020


# In[88]:


car2


# In[90]:


car3 = car.copy()


# In[91]:


car


# In[92]:


del car2


# In[93]:


car


# In[94]:


car3


# In[95]:


del car['brand']


# In[96]:


car


# In[97]:


car3


# In[ ]:




