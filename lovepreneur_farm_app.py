
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="LOVEPRENEUR FARM", layout="wide")

# Logo
try:
    st.image("244306.png", width=180)
except:
    st.title("LOVEPRENEUR FARM")

st.title("LOVEPRENEUR FARM")
st.subheader("Livestock Activities & Inventory Management")

tab1, tab2, tab3 = st.tabs(["Daily Activities", "Inventory", "Dashboard"])

with tab1:
    st.header("Record Daily Livestock Activities")
    with st.form("activity_form"):
        activity_date = st.date_input("Date", date.today())
        livestock_type = st.selectbox(
            "Livestock Type",
            ["Poultry", "Goat", "Sheep", "Pig", "Cattle", "Fish"]
        )
        activity = st.text_area("Activity Performed")
        submitted = st.form_submit_button("Save Activity")

        if submitted:
            st.success("Activity recorded successfully!")

with tab2:
    st.header("Inventory Management")

    item = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=0)
    unit = st.selectbox("Unit", ["Kg", "Bag", "Litre", "Piece"])

    if st.button("Add Inventory"):
        st.success(f"{item} added to inventory.")

with tab3:
    st.header("Farm Dashboard")

    data = pd.DataFrame({
        "Category": ["Feed", "Medicine", "Eggs Produced"],
        "Value": [50, 12, 320]
    })

    st.dataframe(data, use_container_width=True)
    st.metric("Livestock Count", 250)
    st.metric("Inventory Items", 15)

st.sidebar.header("LOVEPRENEUR FARM")
st.sidebar.info("Farm management system for livestock and inventory tracking.")
