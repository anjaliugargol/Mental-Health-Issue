import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error, accuracy_score, auc, classification_report, confusion_matrix, roc_curve, RocCurveDisplay

df = pd.read_csv('cleaned_mental_health.csv')
#print(df.head())
#print(df.tail())

#print(df.info())
#print(df.shape)

df = df.fillna("")

#print(df.isnull().sum())
print(df.nunique())
print(df.columns.to_list())

df.to_csv("cleaned_mh.csv", index=False, encoding="utf-8")



#EDA Analysis

#Univariate Analysis

#Distribution of Mental Health Status
'''df['status'].value_counts()
plt.figure()
sns.countplot(x='status', data=df)
plt.title("Univariate Analysis: Mental Health Status Distribution")
plt.xlabel("Mental Health Category")
plt.ylabel("Count")
plt.show()'''


#Text Length Distribution
df['text_length'] = df['statement'].apply(len)
df['text_length'].describe()

'''plt.figure()
sns.histplot(df['text_length'], bins=40, kde=True)
plt.title("Univariate Analysis: Text Length Distribution")
plt.xlabel("Text Length (Characters)")
plt.ylabel("Frequency")
plt.show()
'''

#Word Count Distribution
df['word_count'] = df['statement'].apply(lambda x: len(x.split()))
df['word_count'].describe()

'''plt.figure()
sns.histplot(df['word_count'], bins=40, kde=True)
plt.title("Univariate Analysis: Word Count Distribution")
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.show()
'''

#Bivariate Analysis

#Mental Health Status vs Text Length
df.groupby('status')['text_length'].mean()
'''plt.figure()
sns.barplot(x='status', y='text_length', data=df)
plt.title("Bivariate Analysis: Status vs Text Length")
plt.xlabel("Mental Health Category")
plt.ylabel("Average Text Length")
plt.show()
'''

#Mental Health Status vs Word Count
df.groupby('status')['word_count'].mean()
'''plt.figure()
sns.boxplot(x='status', y='word_count', data=df)
plt.title("Bivariate Analysis: Status vs Word Count")
plt.xlabel("Mental Health Category")
plt.ylabel("Word Count")
plt.show()
'''

#Text Length vs Word Count
'''plt.figure()
sns.scatterplot(x='text_length', y='word_count', data=df)
plt.title("Bivariate Analysis: Text Length vs Word Count")
plt.xlabel("Text Length")
plt.ylabel("Word Count")
plt.show()
'''

#Multivariate Analysis
#Correlation Between Numerical Features

'''df[['text_length', 'word_count']].corr()
plt.figure()
sns.heatmap(df[['text_length', 'word_count']].corr(), annot=True, cmap='coolwarm')
plt.title("Multivariate Analysis: Correlation Matrix")
plt.show()
'''

#Status, Text Length & Word Count Together
'''plt.figure()
sns.scatterplot(
    x='text_length',
    y='word_count',
    hue='status',
    data=df
)
plt.title("Multivariate Analysis: Text Length vs Word Count by Status")
plt.xlabel("Text Length")
plt.ylabel("Word Count")
plt.show()
'''

#Logistic Regression Model


from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics import classification_report

# Features & target
X = df['statement']   # text data
y = df['status']      # target labels

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numerical features (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

print("Predictions:", y_pred)
print("\nClassification Report:\n", classification_report(y_test, y_pred))






#MySql Connection and Database Creation

'''db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anjali@sql'
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mental_health")
db.close()'''


# Connect to MySQL
'''db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="mental_health"
)

if db.is_connected():
    print("✅ Connected to MySQL successfully")

db.close()
'''


import csv


# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="mental_health"
)

cursor = db.cursor()

sql = '''
INSERT INTO mental_h(statement, status)
VALUES (%s, %s)
'''

with open("cleaned_mental_health.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row

    for row in reader:
        cursor.execute(sql, row)

db.commit()
cursor.close()
db.close()

print("CSV data inserted into MySQL successfully!")

