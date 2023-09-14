[Port](imagen.png)
# Credit Card Fraud Detection Model

This repository contains a credit card fraud detection model implemented in Python using the scikit-learn library. The model is designed to detect fraudulent transactions by employing a Random Forest Classifier, a supervised learning algorithm.

The dataset used for training and testing the model is the Credit Card Fraud Detection dataset sourced from Kaggle. It comprises a total of 284,315 transactions, of which 492 (0.17%) are labeled as fraudulent.

**Dataset Source**: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Model Overview

The model employs a Random Forest Classifier, which excels at handling complex data and is well-suited for classification tasks. To address the imbalanced nature of the credit card fraud dataset, Synthetic Minority Over-sampling Technique (SMOTE) is utilized.

## Model Performance

On the test set, the model demonstrates impressive performance metrics:

- Accuracy: 99.98%
- Precision: 99.97%
- Recall: 1

## Deployment

The model is deployed using Streamlit, a powerful tool for building interactive web applications for machine learning models. Users can input V1-V28 features along with the normalized amount, and the model predicts whether the transaction is fraudulent or legitimate.

> Note: V1-V28 features may be the result of PCA dimensionality reduction to protect user identities and sensitive information.

## Conclusion

This fraud detection model showcases the effectiveness of the Random Forest Classifier, especially when combined with techniques like SMOTE for handling imbalanced data. The high accuracy, precision, and recall scores demonstrate its robustness in identifying fraudulent transactions.

---