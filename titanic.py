#
# Kevin
# Titanic Practice
#

# Titanic
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('titanic.csv')

# Inspect structure
df.shape
df.info()

df.describe()

df.isnull().sum()

# Add missing values and add median in age column
df1 = df.copy()
df1["Age"] = df["Age"].mean()
df1.isnull().sum()

# Drop missing value in cabin and embarked
df1 = df1.dropna()
df1.isnull().sum()


# Count by value
df1['Sex'].value_counts()

import seaborn as sns
sns.countplot(x='Sex', data=df1,)
plt.title('Gender')
plt.show()

df1[['Sex']].plot.line()
plt.show()

# By group
df1['Age'].mean()

# By group
df.groupby(['Pregnancies', 'Outcome']).mean()
df.groupby(['Pregnancies', 'Outcome']).value_counts()
df.groupby(['Pregnancies', 'Outcome']).value_counts(normalize = True)

# Import plt 
import matplotlib.pyplot as plt

# Visual BMI
df[['BMI', 'Glucose']].plot.line()
plt.title('Kevin')
plt.show()


df[['BMI', 'Glucose']].plot.line(figsize=(20, 10), color={"BMI": "red", "Glucose": "blue"})
plt.show()