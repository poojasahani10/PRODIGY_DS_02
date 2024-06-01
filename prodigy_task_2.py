# -*- coding: utf-8 -*-
"""Prodigy Task 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17kOWaY-0Lxw-PUMFMVkwjTwq8XVls0YG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
url = "train.csv"  # Make sure this file is available in the same directory or adjust the path
titanic_df = pd.read_csv(url)

# Display the first few rows of the dataset
print(titanic_df.head())

# Check for missing values
print(titanic_df.isnull().sum())

# Handling missing values
# Fill missing values in the 'Age' column with the median
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)

# Explore the distribution of numerical features
sns.histplot(titanic_df['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.show()

# Explore the distribution of categorical features
sns.countplot(x='Sex', data=titanic_df)
plt.title('Distribution of Gender')
plt.show()

# Explore the relationship between variables
sns.scatterplot(x='Age', y='Fare', data=titanic_df, hue='Survived', palette='Set1')
plt.title('Scatterplot of Age and Fare by Survival')
plt.show()

# Explore survival rates across different categories
sns.barplot(x='Pclass', y='Survived', data=titanic_df, hue='Sex', palette='viridis')
plt.title('Survival Rates by Passenger Class and Gender')
plt.show()

# Correlation matrix
# Select only numerical features for correlation matrix
numerical_features = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
correlation_matrix = titanic_df[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()