import streamlit as st
import pandas as pd

df = pd.read_csv('apps.csv')

st.title('Covid-19 Vaccination Progress Analysis')
st.markdown('![alt text](http://www.coe.int/documents/2323735/7720949/Covid-Vaccine+bioethics.jpg/2b76386f-4455-ed65-273e-9328144faada)')

st.dataframe(df)

sidebar = st.sidebar

sidebar.header('Choose Your Action')