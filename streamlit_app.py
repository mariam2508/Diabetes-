import streamlit as st
import pickle

st.title("🎈Diabetes")

Glucose = st.number_input('Glucose', min_value=0.0, max_value=199.0, value=0.0)
Pregnancies = st.number_input('Pregnancies', min_value=0.0, max_value=17.0, value=0.0)
BMI = st.number_input('BMI', min_value=0.0, max_value=67.1, value=0.0)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

output = model.predict([[Glucose, Pregnancies, BMI]])
st.write("The predicted outcome for Diabetes:", output[0])
