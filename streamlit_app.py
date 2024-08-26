import streamlit as st
import pickle

st.title("🎈Diabetes")

input_features = [[Glucose, Pregnancies, BMI]]

Glucose = st.number_input('Glucose', min_value=0.000, max_value=199.000, value=0.000)
Pregnancies = st.number_input('Pregnancies', min_value=0.000, max_value=17.000, value=0.000)
BMI = st.number_input('BMI', min_value=0.000, max_value=67.100, value=0.000)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

output = model.predict([[Glucose, Pregnancies, BMI]])
st.write("The predicted outcome for Diabetes:", output[0])
