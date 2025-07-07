import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv("regression_data.csv")

# Data
x = dataset["YearsExperience"]
y = dataset["Salary"]

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

# Plot
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="blue")
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(1.25, 55000,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Model of Years Experience vs Salary")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()



