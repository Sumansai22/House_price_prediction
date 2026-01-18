import pandas as pd
import pickle as pk
import streamlit as st



model = pk.load(open(r"C:\Users\Sumanth\OneDrive\Desktop\house prediction model\House_prediction_model.pk1", "rb"))

user_input = pd.DataFrame([['Electronic City Phase II',1000.0,3.0,2.0,3]],columns=['location','total_sqft','bath','balcony','bedrooms'])
st.header('house price prediction')
data = pd.read_csv('C:/Users/Sumanth/OneDrive/Desktop/house prediction model/cleaned_data.csv')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total sqft')
beds = st.number_input('Enter No of Bedrooms')
bath = st.number_input('Enter No of Bathrooms')
balcony = st.number_input('Enter No of balconies')

input = pd.DataFrame([[loc,sqft,bath,balcony,beds]])

if st.button("predict price"):
    output = model.predict(user_input)
    st.success(f'Price of the House is {int(output[0]*100000)}')

