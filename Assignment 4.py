#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

def fun(n):
    return (n*3)


# In[6]:


list(map(fun,[1,3,4,5,6,9]))


# In[8]:


# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

def square(num1):
    return num1**2

sample_list = [4, 5, 2, 9]

result = list(map(square,sample_list))
print("Output = ", result)


# In[11]:


# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

input = lambda x : x+25
print('Output = ', input(10))


# In[ ]:




