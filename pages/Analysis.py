import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config('Analysis')
df = pd.read_csv('datasets/dataviz1.csv')
group_df = df.groupby('sector').mean(numeric_only=True)[['price','avg._price','build_up_area','latitude','longitude']] 
st.header('Avg. Price of Flats')
fig = px.scatter_mapbox(group_df,zoom=10,lat='latitude',lon='longitude',color='avg._price',size='build_up_area',color_continuous_scale='Viridis',mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)

st.header('Area vs Price')
sector_selected = st.selectbox('Sector',['All']+df['sector'].unique().tolist())
if sector_selected=='All':
    st.text('Note: The y-axis is on a logarithmic scale.')
    fig1 = px.scatter(df,x='build_up_area',y='price',color='bhk',log_y=True)
else:
    fig1 = px.scatter(df[df['sector']==sector_selected],x='build_up_area',y='price',color='bhk')
st.plotly_chart(fig1,use_container_width=True)

st.header('Impact of BHK and Furnishing on Price')
df_temp = df[['bhk','furnishing','price']].copy()
df_temp['bhk'] = df_temp['bhk'].apply(lambda x: 'BHK '+str(x))
df_temp = df_temp[df_temp['bhk'] !='BHK 9']
df_temp['furnishing']=df_temp['furnishing'].astype(str).str.replace('0','Unfurnished').str.replace('1','Semi Furnished').str.replace('2','Fully Furnished')
gr_df = df_temp.groupby(['bhk','furnishing'])['price'].median().reset_index()
gr_df['price'] =gr_df['price'].apply(lambda x: str(round(x/100000,2)) + ' Lakh')
fig2 = px.sunburst(gr_df,path=['bhk','furnishing','price'],width=1000,height=1000)
st.plotly_chart(fig2,use_container_width=True)

st.subheader('Side by Side BHK Price Comparision')
fig3=px.box(df[df['bhk']<5],x='bhk',y='price',log_y=True,color='furnishing')
st.plotly_chart(fig3)