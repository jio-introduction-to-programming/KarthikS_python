Topic 1: Modules / Packages

## Research: 
Python is a versatile programming language that allows developers to organize their code into reusable and manageable components. Two essential concepts in Python that facilitate this organization are modules and packages. They play a crucial role in structuring code, promoting code reusability, and simplifying the development process.

## Implementation: 
- Create a Python module named "math_operations.py" that contains functions for basic mathematical operations such as addition, subtraction, multiplication, and division. Import this module into another Python script and demonstrate the usage of its functions.
- A module is a Python file containing Python definitions and statements. It acts as a self-contained unit that can be reused across multiple projects. Modules help in organizing code logically, promoting better code management, and enhancing code readability.
- A package is a collection of related Python modules grouped together in a directory. The primary purpose of packages is to organize code hierarchically, making it easier to manage larger projects. Packages contain a special file named "init.py," which indicates that the directory should be treated as a Python package.

Creating a Module:
To create a module, we simply need to create a Python file with the desired functions, classes, or variables. Let's illustrate this with an example. Consider a module named "math_operations.py":

# math_operations.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero!")


to use the above code we first need to import the module into our Python script.

# main.py

import math_operations

result_add = math_operations.add(5, 3)
print("Addition:", result_add)

result_subtract = math_operations.subtract(5, 3)
print("Subtraction:", result_subtract)

result_multiply = math_operations.multiply(5, 3)
print("Multiplication:", result_multiply)

result_divide = math_operations.divide(5, 3)
print("Division:", result_divide)


## Exploration: 
- Research and explore popular third-party packages available in the Python Package Index (PyPI). Choose one package that interests you and explain its purpose, functionality, and how to install and use it in your Python projects.

scikit-learn, commonly abbreviated as sklearn, is an open-source Python library designed to provide simple and efficient tools for data mining, data analysis, and machine learning. It is built on top of other Python libraries like NumPy, SciPy, and matplotlib, making it an integral part of the data science ecosystem in Python.
The main purpose of scikit-learn is to make machine learning accessible to a wide audience, from beginners to experienced data scientists. It offers a consistent and user-friendly API, making it easy to experiment with various machine learning algorithms and techniques. Some key functionalities of scikit-learn include:
Supervised Learning: scikit-learn provides various algorithms for supervised learning tasks, where the model is trained on labeled data to make predictions on unseen data. It includes algorithms for classification (e.g., logistic regression, decision trees, support vector machines) and regression (e.g., linear regression, random forests).
Unsupervised Learning: For unsupervised learning tasks, scikit-learn offers algorithms for clustering (e.g., k-means, hierarchical clustering) and dimensionality reduction (e.g., principal component analysis).
Model Selection: It provides tools for model selection, including methods for hyperparameter tuning, cross-validation, and performance evaluation.
Preprocessing: scikit-learn offers a range of data preprocessing tools like scaling, encoding categorical variables, and handling missing values.
Ensemble Methods: It includes ensemble methods such as random forests, gradient boosting, and bagging to combine multiple models and improve predictive performance.

to install pip install scikit-learn

one small example 
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions on new data
new_data = np.array([[6], [7]])
predictions = model.predict(new_data)

print("Predictions:", predictions)
