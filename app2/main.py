import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("photo.jpg")

with col2:
    st.title("Shubham Shinde")
    content = """
    Hi, I am Shubham! I am a Python programmer,
    """
    st.info(content)