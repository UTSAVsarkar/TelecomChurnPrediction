import streamlit as st
from about import about
from predict_page import show_predict_page
from explore_page import show_explore_page

st.title("Predict and Explore the data 🤟")

aboutPage, predictPage, explorePage = st.tabs(["About", "Predict", "Explore"])

with aboutPage:
   about()

with predictPage:
   show_predict_page()

with explorePage:
   show_explore_page()