
import streamlit as st
import requests

st.title("SuperKart Sales Prediction")

st.write("Enter the product and store details to predict product sales.")

product_weight = st.number_input("Product Weight", min_value=0.0)
product_allocated_area = st.number_input("Product Allocated Area", min_value=0.0)
product_mrp = st.number_input("Product MRP", min_value=0.0)
store_establishment_year = st.number_input(
    "Store Establishment Year",
    min_value=1900,
    max_value=2100,
    value=2000
)

if st.button("Predict Sales"):
    st.info("Prediction interface is ready.")
