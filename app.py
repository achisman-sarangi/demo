import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open("df.pkl",'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#web app
st.title("Job Recomendation System")
