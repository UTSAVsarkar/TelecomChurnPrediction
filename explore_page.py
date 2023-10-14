import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_explore_page():
    dataset = pd.read_csv('Customer-Churn.csv')

    st.write("""### Churn Count""")
    dataset['Churn'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.write("""### Gender Count""")
    dataset['gender'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.write("""### Contracts Count""")
    dataset['Contract'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.write("""### Internet Service Count""")
    dataset['InternetService'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.write("""### Joint Map""")
    services = ['PhoneService','MultipleLines','InternetService','OnlineSecurity',
           'OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']

    fig, axes = plt.subplots(nrows = 3,ncols = 3,figsize = (15,20))
    for i, item in enumerate(services):
        if i < 3:
            ax = dataset[item].value_counts().plot(kind = 'bar',ax=axes[i,0],rot = 0)
            
        elif i >=3 and i < 6:
            ax = dataset[item].value_counts().plot(kind = 'bar',ax=axes[i-3,1],rot = 0)
            
        elif i < 9:
            ax = dataset[item].value_counts().plot(kind = 'bar',ax=axes[i-6,2],rot = 0)
        ax.set_title(item)
    st.pyplot(plt.gcf())

    st.write("""### Contracts Vs Churn Rates""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Contract','Churn']).size().unstack()
    plt.ylabel(' ')
    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0, 
                                                                    figsize = (18,13),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Churn')
    ax.set_ylabel('% Customers',size = 14)
    ax.set_title('Churn by Contract Type',size = 14)

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())
    
    st.write("""### Phone Service Vs Churn Rates""")
    pie_PhoneService_Yes = pd.DataFrame(dataset[dataset['PhoneService'] == "Yes"]['Churn'].value_counts())
    pie_PhoneService_Yes.plot.pie(subplots=True, labels = pie_PhoneService_Yes.index.values, autopct='%1.1f%%', startangle= 50 )
    plt.ylabel(' ')
    plt.gca().set_aspect('equal')
    st.pyplot(plt.gcf())

    st.write("""### No Phone Service Vs Churn Rates""")
    pie_PhoneService_No = pd.DataFrame(dataset[dataset['PhoneService'] == "No"]['Churn'].value_counts())
    pie_PhoneService_No.plot.pie(subplots=True, labels = pie_PhoneService_Yes.index.values, autopct='%1.1f%%', startangle= 50)
    plt.ylabel(' ')
    plt.gca().set_aspect('equal')
    st.pyplot(plt.gcf())

    st.write("""### Contracts Vs Churn Rates""")    
    pie_Contract_m2m = pd.DataFrame(dataset[dataset['Contract'] == "Month-to-month"]['Churn'].value_counts())
    pie_Contract_m2m.plot.pie(subplots=True, labels = pie_Contract_m2m.index.values, autopct='%1.1f%%', startangle= 75)
    plt.title('Month to Month Contract')
    plt.ylabel(' ')
    plt.gca().set_aspect('equal')
    st.pyplot(plt.gcf())


    pie_Contract_1y = pd.DataFrame(dataset[dataset['Contract'] == "One year"]['Churn'].value_counts())
    pie_Contract_1y.plot.pie(subplots=True, labels = pie_Contract_1y.index.values, autopct='%1.1f%%', startangle= 20)
    plt.title('One Year Contract')
    plt.ylabel(' ')
    plt.gca().set_aspect('equal')
    st.pyplot(plt.gcf())


    pie_Contract_2y = pd.DataFrame(dataset[dataset['Contract'] == "Two year"]['Churn'].value_counts())
    pie_Contract_2y.plot.pie(subplots=True, labels = pie_Contract_2y.index.values, autopct='%1.1f%%', startangle= 5)
    plt.title('Two Year Contract')
    plt.ylabel(' ')
    plt.gca().set_aspect('equal')
    st.pyplot(plt.gcf())