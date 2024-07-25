import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Define column names explicitly
column_names = [
    'Patient_ID', 'Patient_Age', 'Patient_Gender', 
    'Patient_Blood_Pressure', 'Patient_Heartrate', 'Heart-Disease'
]

# Load dataset with header names
df = pd.read_csv(r"dataset.csv", header=None, names=column_names)

# Print column names to debug
print("Column names in the dataset:", df.columns)

# Convert target column to numerical values
df['Heart-Disease'] = df['Heart-Disease'].map({'Heart-Disease': 1, 'No-Disease': 0})

# Features and target variable
X = df[['Patient_ID', 'Patient_Age', 'Patient_Gender', 'Patient_Blood_Pressure', 'Patient_Heartrate']]
y = df['Heart-Disease']

# Create training and testing vars, usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Fit the model on the training data
model = RandomForestClassifier()
model.fit(X_train, Y_train)

# Make predictions on validation dataset
predictions = model.predict(X_test)

# Pickle model
with open(r'new_model.pickle', 'wb') as f:
    pickle.dump(model, f)

# Unpickle model
with open(r'new_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Take input from user
Patient_ID = int(input("Enter Patient_ID: "))
Patient_Age = int(input("Enter Patient_Age: "))
Patient_Gender = int(input("Enter Patient_Gender: "))
Patient_Blood_Pressure = int(input("Enter Patient_Blood_Pressure: "))
Patient_Heartrate = int(input("Enter Patient_Heartrate: "))

# Define columns for prediction
columns = ['Patient_ID', 'Patient_Age', 'Patient_Gender', 'Patient_Blood_Pressure', 'Patient_Heartrate']
features = pd.DataFrame([[Patient_ID, Patient_Age, Patient_Gender, Patient_Blood_Pressure, Patient_Heartrate]],
                        columns=columns)

# Make prediction
result = model.predict(features)
print("Prediction:", result[0])