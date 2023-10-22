import streamlit as st
st.set_page_config('Home')
st.header('Campusx Real Estate Project')
st.markdown("<p style='font-weight: bold;'>Welcome to Our Housing Data Project</p>", unsafe_allow_html=True)
st.text('''
This project is a culmination of efforts to gather, preprocess, and analyze housing data from Housing.com. It encompasses various features, including a recommender, price predictor, and in-depth analysis tools.''')
st.markdown("<p style='font-weight: bold;'>About the Project</p>", unsafe_allow_html=True)

st.text('''
Data Collection: In this project I collected data from Housing.com, a prominent real estate platform, to create a robust dataset for analysis and modeling.

Preprocessing: The gathered data went through extensive preprocessing to clean, format, and prepare it for analysis. This step ensures the accuracy and reliability of our results.

Model Training: This project leveraged machine learning techniques to develop models that power our recommender and price prediction tools. These models are trained on the processed housing data.''')
st.markdown("<p style='font-weight: bold;'>Tools Available</p>", unsafe_allow_html=True)
st.text('''
Recommender: This tool uses the power of machine learning to provide personalized housing recommendations based on user preferences.

Price Predictor: Get an estimate of housing prices based on various features parameters.

In-depth Analysis: Dive deep into the housing data with our analysis tools. Explore trends, patterns, and gain valuable insights.''')

st.markdown("<p style='font-weight: bold;'>Educational Purpose</p>", unsafe_allow_html=True)

st.text('''It's important to note that the data used in this project is strictly for educational purposes. The project aims to demonstrate data collection, preprocessing, and machine learning techniques in a real-world context.
''')
