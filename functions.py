import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import joblib

data = pd.read_csv('data/raw/Employee-Attrition.csv')


def clean_data(data: pd.DataFrame) -> pd.DataFrame:

    # Convert Attrition from Yes/No to binary values
    data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})

    # Convert OverTime from Yes/No to binary values
    data['OverTime'] = data['OverTime'].map({'Yes': 1, 'No': 0})

    # Encode BusinessTravel as ordered numerical values based on travel frequency
    data['BusinessTravel'] = data['BusinessTravel'].map({
        'Non-Travel': 0,
        'Travel_Rarely': 1,
        'Travel_Frequently': 2})

    # Create a new feature for yearly salary based on the monthly income
    data['yearly_salary'] = data['MonthlyIncome'] * 12

    # Drop columns that are not useful for modeling
    data = data.drop(columns=['StandardHours', 'Over18', 'EmployeeCount'])
    
    # Convert all remaining string type columns to category to help save memory and performance
    string_columns = data.select_dtypes('object').columns.to_list()

    # Apply one-hot encoding to the remaining string type columns
    data = pd.get_dummies(data=data, columns=string_columns)
    
    return data

def train_logistic_regression_model(data: pd.DataFrame):

    # Split the data into features and target variable
    X = data.drop(columns='Attrition')
    y = data['Attrition']

    # Split the data into training and testing sets with stratification on the target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=123, test_size=.3)

    # Create a pipeline for the logistic regression model with standard scaling
    lr_model = Pipeline([
    ('scaler', StandardScaler()),
    ('logistic_regression', LogisticRegression())
    ])

    # Fit the logistic regression model using the training data
    lr_model.fit(X_train, y_train)

    # Predict probabilities for the test set using the trained model
    lr_y_proba = lr_model.predict_proba(X_test)[:, 1]

    # Calculate the ROC AUC score for the test set predictions
    lr_roc_auc = roc_auc_score(y_test, lr_y_proba)

    # Train the logistic regression model using the pipeline
    lr_y_pred = lr_model.predict(X_test)

    # Save the trained model to a file
    joblib.dump(lr_model, 'models/logistic_regression_model.pkl')

    # Return the trained model
    return lr_model, lr_roc_auc, lr_y_pred, y_test, X

def dashboard_dataset(data: pd.DataFrame, lr_model, X: pd.DataFrame) -> pd.DataFrame:

    # Generate prediction probabilities for the dashboard dataset using the trained logistic regression model
    proba = pd.DataFrame(
        lr_model.predict_proba(X),
        columns=['Stay_Probability', 'Leave_Probability'],
        index=data.index
    )

    # Concatenate the original data with the prediction probabilities for the dashboard
    return pd.concat([data, proba], axis=1)