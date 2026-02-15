import streamlit as st
import random
from questions import questions

st.title("🎉 Friends Question Generator")

st.write("Select a category and click the button to get a random question!")

category = st.selectbox("Choose Category", list(questions.keys()))

if st.button("Get Question 🎲"):
    st.success(random.choice(questions[category]))
