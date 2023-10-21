import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config('Recommender')
df = pd.read_csv('data/df.csv')
latlong= pd.read_csv('data/latlong.csv')
def recommend_build(col_,value,data):
    data[str(col_ + '_subtract')] = np.abs(data[col_] - value)
    return data.sort_values(by=[str(col_ + '_subtract')])
def recommend_location(lat,long,data):
    data['distance']= np.abs(data['latitude'] - lat) + np.abs(data['longitude']-long)
    return data.sort_values(by=['distance'])
def recommender_(user_input,data=df.copy()):
    recommend= dict()
    j = 0
    for i in ['build_up_area', 'avg._price', 'floor', 'age_of_property', 'furnishing','bhk', 'parking','possession_status']:
        val = recommend_build(i,user_input[j],data).index
        val = np.array(val).reshape(1,7997)[0][:100]
        s = [1,0.9,0.3,0.3,0.3,0.2,0.2,0.2,.3]
        for k in val:
            if k in recommend.keys():
                recommend[k] = recommend[k] + s[j]
            else:
                recommend[k] = s[j]
        j=j+1
    val = recommend_location(user_input[-2],user_input[-1],data).index
    val = np.array(val).reshape(1,7997)[0][:100]
    for k in val:
        if k in recommend.keys():
            recommend[k] = recommend[k] + 1
        else:
            recommend[k] = 1
    return list(dict(sorted(recommend.items(),key=lambda item:item[1],reverse=True)).keys())[:10]

st.header('Recommender')

# Create input fields for the user to enter the features of the house
build_up = st.number_input('Build Up Area (sq ft)', min_value=1)
price = st.number_input('Price')
floor = st.number_input('Floor', min_value=0)
age = st.number_input('Age of the house (years)', min_value=0)
sector = st.selectbox('Sector',latlong['sector'].values)
furnishing = st.selectbox('Furnishing', ['Unfurnished','Semi Furnished','Fully Furnished'])
bhk = st.number_input('BHK', min_value=0)
possession_status = st.number_input('Possession Status', min_value=0)
parking = st.number_input('Parking',min_value=0)
arr = latlong[latlong['sector'] ==(sector)][['latitude','longitude']].values.reshape(2)

recommend_button = st.button('Recommend')

user_input = [build_up,price/build_up,floor,age,(lambda x:0 if x== 'Unfurnished' else 1 if x=='Semi Furnished' else 2)(furnishing),bhk,parking,possession_status,arr[0],arr[1]]
if recommend_button:
    links=df.loc[recommender_(user_input,df.copy())]['link'].values
    col1, col2 = st.columns(2)
    with col1:
        col1.write(f"[{links[0]}]({links[0]})", unsafe_allow_html=True)
        col1.write(f"[{links[1]}]({links[1]})", unsafe_allow_html=True)
        col1.write(f"[{links[2]}]({links[2]})", unsafe_allow_html=True)
        col1.write(f"[{links[3]}]({links[3]})", unsafe_allow_html=True)
        col1.write(f"[{links[4]}]({links[4]})", unsafe_allow_html=True)
    with col2:
        col2.write(f"[{links[5]}]({links[5]})", unsafe_allow_html=True)
        col2.write(f"[{links[6]}]({links[6]})", unsafe_allow_html=True)
        col2.write(f"[{links[7]}]({links[7]})", unsafe_allow_html=True)
        col2.write(f"[{links[8]}]({links[8]})", unsafe_allow_html=True)
        col2.write(f"[{links[9]}]({links[9]})", unsafe_allow_html=True)