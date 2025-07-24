import seaborn as sns
import streamlit as st

st.title("✅ Seaborn Test App")
df = sns.load_dataset("iris")
st.write(df.head())
