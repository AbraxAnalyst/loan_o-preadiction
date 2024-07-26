# loan Preadiction
![](LOAN.jpg)
## Problem Statement
In the current financial landscape, accurately predicting loan defaults is crucial for minimizing risks and optimizing decision-making processes for lending institutions. Given the diverse factors that influence a borrower's likelihood to default, it is essential to build a predictive model that can analyze these factors and forecast the probability of loan defaults effectively.
This project aims to develop a machine learning model to predict the default status of loans based on a variety of borrower attributes, including age, income, home ownership, employment duration, loan intent, loan grade, loan amount, interest rate, loan term, historical default status, credit history length, and current loan status. By leveraging this model, lending institutions can make more informed decisions, reduce financial losses, and improve their overall risk management strategies.
Interact with Loan predictor model : https://loan-preadiction-1.onrender.com/
### Approach used in the project
1. Data Exploration and Preprocessing
2. Data Cleaning
3. Feature Engineering
4. Model Building
5. Model Evaluation
6. Deployment
7. Monitoring and Maintenance

### The Dataset
The dataset utilized in this study pertains to loan prediction and encompasses various attributes that potentially influence the likelihood of a loan default and it’s gotten from  kaggle. Below is an overview of the dataset attributes:
- customerID: Unique identifier for each customer.
- customer_age: Age of the customer.
- customer_income: Annual income of the customer.
- home_ownership: Home ownership status of the customer (e.g., Rent, Own).
- employment_duration: Duration of the customer's employment in years.
- loan_intent: The purpose for which the loan is intended (e.g., Education, Medical, Personal).
- loan_grade: The grade assigned to the loan based on creditworthiness.
- loan_amnt: The loan amount requested by the customer.
- loan_int_rate: The interest rate applicable to the loan.
- term_years: The duration of the loan term in years.
- historical_default: Binary indicator of whether the customer has defaulted on loans historically.
- cred_hist_length: The length of the customer's credit history in years.
- current_loan_status: The current status of the loan (e.g., Active, Default).

### Analysis
#### Data Exploration and Data Cleaning
I Visualize and summarize the dataset to understand the distribution of variables, detect patterns, and identify correlations.
I Generate descriptive statistics to gain insights into the characteristics of the data.
Handle missing values using appropriate techniques such as imputation or removal. I removed the entries with more than 20% null value and remove the attributes with more than 60%
Detect and treat outliers to prevent them from skewing the model's predictions
Convert categorical variables into numerical representations using techniques like one-hot encoding or label encoding. (For this project Label encoding was used)

#### Feature Engineering
Develop new features that might improve the model’s predictive power, such as interaction terms or aggregated features.
Use techniques like correlation analysis, feature importance from tree-based models, or recursive feature elimination to select the most relevant features for the model.
#### Model Building
I Experiment with two machine learning algorithms which are Logistic Regression and XGboost Regressor
I Split the data into training and testing sets to evaluate the performance of different models.
I also engaged the use of cross-validation techniques to ensure that the model generalizes well to unseen data.
 #### Model Evaluation
This project (Model) was evaluated using metrics such as accuracy, precision, recall, F1-score, and Area Under the ROC Curve (AUC-ROC).
I compared the performance of different models and select the best-performing one based on the evaluation metrics.
I used random search techniques to optimize the hyperparameters of the selected model.
 Observation
The base model was created with 80% accuracy, but after Feature engineering using correlation matrix to determine the importance of this attributes to the Loan default. The model accuracy jump from 80% to 84% accuracy.
The model was deployed and the frontend was handled with streamlit package on python.

![first model](first model.png)
