import pickle
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

#import file
dataset = pd.read_csv('Customer-Churn.csv')

#remove useless data
dataset = dataset.drop(columns = ['customerID', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen'])

#re-arrange the columns
multipleLines = dataset.pop('MultipleLines')
internetService = dataset.pop('InternetService')
contract = dataset.pop('Contract')
tenure = dataset.pop('tenure')

dataset.insert(0, "MultipleLines", multipleLines)
dataset.insert(0, "InternetService", internetService)
dataset.insert(0, "Contract", contract)
dataset.insert(0, "tenure", tenure)

#divide the dataset
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#encode please
Contract = LabelEncoder()
dataset['Contract'] = Contract.fit_transform(dataset['Contract'])

InternetService = LabelEncoder()
dataset['InternetService'] = InternetService.fit_transform(dataset['InternetService'])

MultipleLines = LabelEncoder()
dataset['MultipleLines'] = MultipleLines.fit_transform(dataset['MultipleLines'])

gender = LabelEncoder()
dataset['gender'] = gender.fit_transform(dataset['gender'])

Partner = LabelEncoder()
dataset['Partner'] = Partner.fit_transform(dataset['Partner'])

Dependents = LabelEncoder()
dataset['Dependents'] = Dependents.fit_transform(dataset['Dependents'])

PhoneService = LabelEncoder()
dataset['PhoneService'] = PhoneService.fit_transform(dataset['PhoneService'])

OnlineSecurity = LabelEncoder()
dataset['OnlineSecurity'] = OnlineSecurity.fit_transform(dataset['OnlineSecurity'])

OnlineBackup = LabelEncoder()
dataset['OnlineBackup'] = OnlineBackup.fit_transform(dataset['OnlineBackup'])

DeviceProtection = LabelEncoder()
dataset['DeviceProtection'] = DeviceProtection.fit_transform(dataset['DeviceProtection'])

TechSupport = LabelEncoder()
dataset['TechSupport'] = TechSupport.fit_transform(dataset['TechSupport'])

StreamingTV = LabelEncoder()
dataset['StreamingTV'] = StreamingTV.fit_transform(dataset['StreamingTV'])

StreamingMovies = LabelEncoder()
dataset['StreamingMovies'] = StreamingMovies.fit_transform(dataset['StreamingMovies'])

PaperlessBilling = LabelEncoder()
dataset['PaperlessBilling'] = PaperlessBilling.fit_transform(dataset['PaperlessBilling'])

Churn = LabelEncoder()
dataset['Churn'] = Churn.fit_transform(dataset['Churn'])


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#ML Time 😎
model = DecisionTreeClassifier(random_state=1)
model.fit(X,y)

#save model
data = {
   "model" : model,
   "Contract": Contract,
   "InternetService": InternetService,
   "MultipleLines": MultipleLines,
   "gender": gender,
   "Partner": Partner,
   "Dependents": Dependents,
   "PhoneService": PhoneService,
   "OnlineSecurity": OnlineSecurity,
   "OnlineBackup": OnlineBackup,
   "DeviceProtection": DeviceProtection,
   "TechSupport": TechSupport,
   "StreamingTV": StreamingTV,
   "StreamingMovies": StreamingMovies,
   "PaperlessBilling": PaperlessBilling,
   }

with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)