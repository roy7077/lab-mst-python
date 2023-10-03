# cook your dish here
// 2.1
import pandas as pd

# Create a Pandas DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)


//
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform some basic operations
mean = np.mean(arr)
sum = np.sum(arr)

# Print the results
print("Mean:", mean)
print("Sum:", sum)

//
from scipy.stats import norm

# Generate random data following a normal distribution
data = norm.rvs(loc=0, scale=1, size=100)

# Calculate the mean and standard deviation
mean = data.mean()
std_dev = data.std()

# Print the results
print("Mean:", mean)
print("Standard Deviation:", std_dev)

//
import matplotlib.pyplot as plt

# Create data for a simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot using Matplotlib
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()








// 2.2 
import math
import numpy as np
import scipy.stats as stats

# math library
x=25
y=math.sqrt(x)
print(y)

# numpy library
data=np.array([1,2,3,4,5])
mean=np.mean(data)
print("mean -> ",mean)

# scipy library
data2=np.array([10,11,12,13,14])
dec=stats.describe(data2)
print(dec)