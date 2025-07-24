import streamlit as st

st.title("Utkarsh srivastava ")

name=st.text_input("Enter your name: ")
age=st.slider("Select your age:",0,100,25)
st.write(f"your age is :{age}.")
if name:
    st.write(f"Hello, {name}")
