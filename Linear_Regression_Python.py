import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()

#!/usr/bin/env python
# coding: utf-8

# Assignment 2: Part 1: Build Linear Regression Models in Jupyter Notebooks- Python

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.

# In[7]:


import pandas as pd


# Imports the pandas library which is a powerful python library used when working with tabular data (like spreadsheets or CSV files).

# In[8]:


dataset = pd.read_csv("regression_data.csv")


# This reads the CSV file and loads the information into a dataframe which can be manipulated in python.

# In[9]:


import matplotlib.pyplot as plt


# This initiates Matplotlib function for plotting data points.

# In[10]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# Scatter plot with X axis being years of experience and y being salary.

# In[11]:


from sklearn.linear_model import LinearRegression 


# This utilizes Sklearn's linear regression function

# In[12]:


model = LinearRegression()


# In[13]:


model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# Generated a linear regresssion model-- performed the coding steps one at a time.

# In[14]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# Combined all coding steps together to develop a linear regression model.

# In[16]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[17]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[18]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# tied all steps together and then performed the overlay of the regression line. 
# 

# In[19]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])


# Above-- 0.78515863 is our R-squared value for our regresssion line to evaluate our model. This consistent with our graphical representation as the plot has a positive correlation. 

# In[ ]:




