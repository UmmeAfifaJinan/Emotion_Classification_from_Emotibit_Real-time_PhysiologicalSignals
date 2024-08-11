import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Step 1: Load Your Historical EmotiBit Data
# Replace 'ecg_data.csv' with the path to our actual EmotiBit data file
ecg_df = pd.read_csv('your_ecg_data.csv')

# Display the first few rows 
print(ecg_df.head())

# Assuming 'Target' is our label column and other columns are our features

# Step 2: Split the Data into Training and Test Sets
train_set, test_set = train_test_split(ecg_df, test_size=0.2, random_state=42)

# Step 3: Prepare the Data
# Define predictors (features) and target
train_predictors = train_set.drop("Target", axis=1)
train_labels = train_set["Target"]

test_predictors = test_set.drop("Target", axis=1)
test_labels = test_set["Target"]

# Step 4: Create a Data Processing Pipeline
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="mean")),
    ('scaler', StandardScaler())
])

num_attribs = list(train_predictors.columns)  # Assuming all are numerical

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs)
])

train_X = full_pipeline.fit_transform(train_predictors)
train_y = train_labels.values

test_X = full_pipeline.transform(test_predictors)
test_y = test_labels.values

# Step 5: Train ML Models
# Initialize models
models = {
    "RandomForest": RandomForestClassifier(random_state=42),
    "SGDClassifier": SGDClassifier(random_state=42),
    "SVC": SVC(random_state=42),
    "KNN": KNeighborsClassifier(),
    "GradientBoosting": GradientBoostingClassifier(random_state=42),
    "LogisticRegression": LogisticRegression(random_state=42)
}

# Train each model
trained_models = {}
for name, model in models.items():
    model.fit(train_X, train_y)
    trained_models[name] = model
    print(f"Trained {name} model.")

# Step 6: Evaluate Models
for name, model in trained_models.items():
    predictions = model.predict(test_X)
    accuracy = accuracy_score(test_y, predictions)
    f1 = f1_score(test_y, predictions)
    print(f"{name} - Accuracy: {accuracy:.2f}, F1 Score: {f1:.2f}")

# Step 7: Save the Models and Scaler
joblib.dump(full_pipeline, 'scaler.pkl')
for name, model in trained_models.items():
    joblib.dump(model, f'{name.lower()}_model.pkl')

print("Models and scaler saved successfully.")
