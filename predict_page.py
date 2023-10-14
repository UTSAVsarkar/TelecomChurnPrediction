import streamlit as st
import pickle
import numpy as np
import re

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
Contract = data["Contract"]
InternetService = data["InternetService"]
MultipleLines = data["MultipleLines"]
gender = data["gender"]
Partner = data["Partner"]
Dependents = data["Dependents"]
PhoneService = data["PhoneService"]
OnlineSecurity = data["OnlineSecurity"]
OnlineBackup = data["OnlineBackup"]
DeviceProtection = data["DeviceProtection"]
TechSupport = data["TechSupport"]
StreamingTV = data["StreamingTV"]
StreamingMovies = data["StreamingMovies"]
PaperlessBilling = data["PaperlessBilling"]

def show_predict_page():
    st.write("""### Please fill the following information""")

    tenure = st.text_input('Tenure', placeholder="Tenure", value = 1)

    dict = {
        'Contract': ['Month-to-month', 'One year', 'Two year'],
        'InternetService': ['DSL', 'Fiber optic', 'No'],
        'MultipleLines': ['No phone service', 'No', 'Yes'],
        'gender': ['Female', 'Male'],
        'Partner': ['Yes', 'No'],
        'Dependents': ['No', 'Yes'],
        'PhoneService': ['No', 'Yes'],
        'OnlineSecurity': ['No', 'Yes', 'No internet service'],
        'OnlineBackup': ['Yes', 'No', 'No internet service'],
        'DeviceProtection': ['No', 'Yes', 'No internet service'],
        'TechSupport': ['No', 'Yes', 'No internet service'],
        'StreamingTV': ['No', 'Yes', 'No internet service'],
        'StreamingMovies': ['No', 'Yes', 'No internet service'],
        'PaperlessBilling': ['Yes', 'No'],
    }

    radioList = []

    for key, value in dict.items():
        radioList.append(
            st.radio(
            re.sub(r'([a-z])([A-Z])', r'\1 \2', key).upper(),
            value,
            horizontal = True
        ))

    ok = st.button("Predict")

    if ok:
        if(tenure == ''):
            st.error('Tenure field is empty!', icon="🚨")
        else:
            listItems = [tenure]
            for x in radioList:
                listItems.append(x)

            inputArr = np.array([listItems])

            inputArr[:, 1] = Contract.transform(inputArr[:, 1])
            inputArr[:, 2] = InternetService.transform(inputArr[:, 2])
            inputArr[:, 3] = MultipleLines.transform(inputArr[:, 3])
            inputArr[:, 4] = gender.transform(inputArr[:, 4])
            inputArr[:, 5] = Partner.transform(inputArr[:, 5])
            inputArr[:, 6] = Dependents.transform(inputArr[:, 6])
            inputArr[:, 7] = PhoneService.transform(inputArr[:, 7])
            inputArr[:, 8] = OnlineSecurity.transform(inputArr[:, 8])
            inputArr[:, 9] = OnlineBackup.transform(inputArr[:, 9])
            inputArr[:, 10] = DeviceProtection.transform(inputArr[:, 10])
            inputArr[:, 11] = TechSupport.transform(inputArr[:, 11])
            inputArr[:, 12] = StreamingTV.transform(inputArr[:, 12])
            inputArr[:, 13] = StreamingMovies.transform(inputArr[:, 13])
            inputArr[:, 14] = PaperlessBilling.transform(inputArr[:, 14])

            churn = model.predict(inputArr)

            if(churn[0] == 0):
                st.subheader("This customer is not likely to churn 😄")
            else:
                st.subheader(f"This customer is likely to churn 😔")
            
            st.write("""### 👈 To know more about Churn, go to About page.""")