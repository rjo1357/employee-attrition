import pandas as pd
from sklearn.metrics import classification_report
from functions import *


def main():

    # Load and clean the data
    data = pd.read_csv('data/raw/Employee-Attrition.csv')
    data = clean_data(data)

    # Train the logistic regression model
    lr_model, lr_roc_auc, lr_y_pred, y_test = train_logistic_regression_model(data)

    # Display model performance
    print('\n', 'Logistic Regression Model Performance:', '\n\n', 52 * '=', '\n', f' ROC_AUC Score: {lr_roc_auc:.2f}', '\n', 52 * '=')

    print('  Classification Report:', '\n', 52 * '=')

    print(classification_report(y_test, lr_y_pred), '\n', 52 * '=')


if __name__ == "__main__":
    main()