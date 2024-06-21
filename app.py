import streamlit as st 
import pandas as pd
import pickle
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
from sklearn.linear_model import LogisticRegression

#import model 
pickle_in = open("model.pkl","rb" )
model = model = pickle.load(pickle_in)

df = pd.read_csv("loany.csv") 

st.title("Loan Predictor")
home_ownership = st.selectbox('Home Ownership Type',['RENT', 'OWN', 'MORTGAGE', 'OTHER'])

loan_intent = st.selectbox('Loan Intent', ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT',
       'DEBTCONSOLIDATION'] )

loan_grade = st.selectbox('Loan Grade',['A', 'B', 'C', 'D', 'E'] )

cred_hist_length = st.number_input(label= "Credict History Length (Years)")

customer_age = st.slider( "Customer Age",18, 60, 25 )
customer_income = st.number_input(label= "How much does the Customer Earn")
employment_duration = st.slider( "Employment Duration", 2, 30, 10)
loan_amnt = st.number_input(label= "Loan Amount")
loan_int_rate = st.number_input(label= "Rate")
term_years = st.number_input(label= "Loan Duration")

if st.button("Predict"):
    
    if home_ownership == 'RENT':
        home_ownership = 0
    elif home_ownership == 'OWN':
        home_ownership = 1
    elif home_ownership == 'MORTGAGE':
        home_ownership = 2
    else:
        home_ownership = 3
# LOAN iNTENT 
    if loan_intent ==  'PERSONAL':
        loan_intent = 0
    elif loan_intent == 'EDUCATION':
        loan_intent = 1
    elif loan_intent == 'MEDICAL':
        loan_intent = 2
    elif loan_intent == 'VENTURE':
        loan_intent = 3
    elif loan_intent == 'HOMEIMPROVEMENT':
        loan_intent = 4
    else:
        loan_intent = 5

#Loan Grade
    if loan_grade == "A":
        loan_grade = 0
    elif loan_grade == "B":
        loan_grade = 1
    elif loan_grade == "C":
        loan_grade == 2
    elif loan_grade == "D":
        loan_grade == 3
    elif loan_grade == "E":
        loan_grade = 4
        
    
    query = np.array([customer_age,customer_income,home_ownership,employment_duration,loan_intent,loan_grade,loan_amnt,loan_int_rate,term_years,cred_hist_length,]).reshape(1,10)
    
    result = model.predict(query)[0]
    
    if result == 0:
        st.title("He will not pay back the loan")
    else:
        st.title("He will pay back, Grant him loan")
