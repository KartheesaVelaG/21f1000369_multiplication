import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write('Multiplication of 2 given numbers.')

option1 = st.selectbox('Select type of first number', ('float', 'integer'))
if (option1=='float'):
    m = st.number_input('Enter first number: ', step=0.01)
else:
    m = st.number_input('Enter first number: ', step=1)

option2 = st.selectbox('Select type of second number', ('float', 'integer'))
if (option2=='float'):
    n = st.number_input('Enter second number: ', step=0.01)
else:
    n = st.number_input('Enter second number: ', step=1)

st.write("The answer is",m*n)