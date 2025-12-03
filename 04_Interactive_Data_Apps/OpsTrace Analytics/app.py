import pandas
import pandas as pd
import streamlit as st
import main


st.title("Log Hunter - FSC")
st.sidebar.header("Filters")

dt = main.load_data("row_data_V2.txt")


dt["Time"] = dt["Time"].astype(str).str.strip()
dt["Time"] = pd.to_datetime(dt["Time"], errors='coerce', utc=True)

min_date = dt["Time"].min()
max_date = dt["Time"].max()

selected_dates = st.sidebar.date_input("Select Date Range", [min_date, max_date])

if len(selected_dates) == 2:
     start_date = selected_dates[0]
     end_date = selected_dates[1]
     dt = dt[(dt["Time"].dt.date >= start_date) & (dt["Time"].dt.date <= end_date)]


dt["Category"] = dt["Category"].str.strip()
dc = ["All"] + dt["Category"].unique().tolist()
selected_cat = st.sidebar.multiselect("Selected Category", dc)

if selected_cat:
    dt = dt[dt["Category"].isin(selected_cat)]


dt["SubCategory"] = dt["SubCategory"].str.strip()
ds = ["All"] + dt["SubCategory"].unique().tolist()
selected_subct = st.sidebar.multiselect("Selected Sub-Category", ds)

if selected_subct:
    dt= dt[dt["SubCategory"].isin(selected_subct)]


dt["Zone"] = dt["Zone"].str.strip()
dz = ["All"] + dt["Zone"].unique().tolist()
selected_mcode = st.sidebar.multiselect("Selected Zone", dz)

if selected_mcode:
    dt= dt[dt["Zone"].isin(selected_mcode)]

dt["PickNumber"] = dt["PickNumber"]
dp = ["All"] + dt["PickNumber"].unique().tolist()
selected_pcknumber = st.sidebar.multiselect("Selected PickNumber", dp)

if selected_pcknumber:
    dt = dt[dt["PickNumber"].isin(selected_pcknumber)]


csv_data = dt.to_csv(index=False).encode('utf-8-sig')

st.download_button(label="Downland Table", data= csv_data, file_name="log_analysis.csv", mime="text/csv")

st.dataframe(dt)
