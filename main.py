import streamlit as st

st.set_page_config(page_title="Scriptify AI", layout="centered")

col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=60)

with col2:
    st.markdown("## Welcome to Scriptify AI!")

st.write("""
Navigate using the sidebar:
- Generate a Script  
- Dashboard (View your scripts)  
- Upgrade to Pro
""")
