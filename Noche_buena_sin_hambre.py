import streamlit as st
import pandas as pd

# Title
st.title("Noche buena sin hambre")

# Text
st.write("My name is Santiago Marin Carrillo")
name = st.text_input("What's your name?")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
st.write("How old are you?")
age = st.slider("Select your age", min_value=0, max_value=100)
st.write(f"Your age is: {age}")

st.write("Noche buena sin hambre is a campaign with the aim of sharing a Christmas dinner with homeless people in the sector.")

st.markdown(" # Noche buena sin hambre 2022 - 2024")

try:
    chart_data = pd.read_excel("Noche_buena_sin_hambre_2022-2024.xlsx")
    st.line_chart(chart_data)
except Exception as e:
    st.error(f"error loading file: {e}")