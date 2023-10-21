import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.set_page_config('Price Predictor')
with open('models/xg.pkl','rb') as f:
   xg = pickle.load(f)
with open('data/sector_values.pkl','rb') as f:
   sector_values = pickle.load(f)
latlong = pd.read_csv('data/latlong.csv')
build_up = st.number_input('Build Up Area (sq ft)', min_value=1)
floor = st.number_input('Floor', min_value=0)
age = st.number_input('Age of the house (years)', min_value=0)
sector = st.selectbox('Sector',sorted(latlong['sector'].unique()))
facing = st.selectbox('Facing',['East Facing', 'North Facing',
       'North East Facing', 'North West Facing',
       'South Facing', 'South East Facing',
       'South West Facing', 'West Facing',])
furnishing = st.selectbox('Furnishing', ['Unfurnished','Semi Furnished','Fully Furnished'])
bhk = st.number_input('BHK', min_value=0)
possession_status = st.number_input('Possession Status', min_value=0)
bathrooms = st.number_input('Bathrooms')
balcony = st.number_input('Balcony')
open_parking = st.number_input('Open Parking',min_value=0)
covered_parking = st.number_input('Covered Parking',min_value=0)
sector = sector_values.get(sector)
input_arr = np.array([np.log(build_up),np.log(floor+1),np.log(age+1),(lambda x: 0 if x=='Unfurnished' else 1 if x == 'Semi Furnished' else 2)(furnishing),bhk,bathrooms,balcony,open_parking,covered_parking,possession_status,sector]).reshape(1,11)
predict = st.button('Predict')
if predict:
    st.write(f'The price of flat is around Rs. {np.exp(xg.predict(input_arr))[0]}')

