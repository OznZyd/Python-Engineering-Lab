import pandas
import pandas as pd
import streamlit as st
import main
import datetime
from datetime import datetime, time

st.set_page_config(layout="wide", page_title="OpsTrace Analytics")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.markdown("")

    st.image("assets/Welcome_Screen.png", use_container_width=True)

    with st.form("login_form"):
        password = st.text_input("🔑 Enter Access Key", type="password", placeholder="••••••••")

        submit_button= st.form_submit_button("🔓Login")

    if submit_button:

        if password == "31082024":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong Password!")
    st.stop()

st.image("assets/Main_Screen.png", use_container_width=True)
st.sidebar.image("assets/SideBar.png", width=600)
st.sidebar.markdown( """
    <h2 style='text-align: left; color: black; font-family: monospace;'>
        🕵️‍♂️ FILTERS
    </h2>
    """,
    unsafe_allow_html=True )


update_files = st.sidebar.file_uploader("Update .log FIles", accept_multiple_files=True)

if update_files:
    all_files = []
    for file in update_files:
        data= main.load_data(file)
        all_files.append(data)
    dt = pd.concat(all_files)
    dt = dt.dropna(axis=1, how='all')

    dt["Time"] = dt["Time"].astype(str).str.strip()
    dt["Time"] = pd.to_datetime(dt["Time"], errors='coerce', utc=True)

    min_date = dt["Time"].min()
    max_date = dt["Time"].max()

    selected_dates = st.sidebar.date_input("Select Date Range", [min_date, max_date])

    co11, co12 = st.sidebar.columns(2)

    with co11:
        start_time = st.time_input("Start Time", value=time(0, 0))
    with co12:
        end_time = st.time_input("End Time", value=time(23, 59))


    if len(selected_dates) == 2:

        dt["Time"] = dt["Time"].dt.tz_localize(None)

        start_date = selected_dates[0]
        end_date = selected_dates[1]
        all_start = datetime.combine(start_date, start_time)
        all_end = datetime.combine(end_date, end_time)

        dt = dt[(dt["Time"] >= all_start) & (dt["Time"] <= all_end)]



    dt["Category"] = dt["Category"].str.strip()
    dc = ["All"] + dt["Category"].unique().tolist()
    selected_cat = st.sidebar.multiselect("Selected Category", dc)

    if selected_cat:
        dt = dt[dt["Category"].isin(selected_cat)]


    dt["Sub-Category"] = dt["Sub-Category"].str.strip()
    ds = ["All"] + dt["Sub-Category"].unique().tolist()
    selected_subct = st.sidebar.multiselect("Selected Sub-Category", ds)

    if selected_subct:
        dt= dt[dt["Sub-Category"].isin(selected_subct)]


    dt["Zone"] = dt["Zone"].str.strip()
    dz = ["All"] + dt["Zone"].unique().tolist()
    selected_zone = st.sidebar.multiselect("Selected Zone", dz)

    if selected_zone:
        dt= dt[dt["Zone"].isin(selected_zone)]

    dt["Pick Number"] = dt["Pick Number"]
    dp = ["All"] + dt["Pick Number"].unique().tolist()
    selected_pcknumber = st.sidebar.multiselect("Selected PickNumber", dp)

    if selected_pcknumber:
        dt = dt[dt["Pick Number"].isin(selected_pcknumber)]

    dt["Barcode Number"] = dt["Barcode Number"].str.strip()
    dz = ["All"] + dt["Barcode Number"].unique().tolist()
    selected_brnumber = st.sidebar.multiselect("Selected Barcode Number", dz)

    if selected_brnumber:
        dt = dt[dt["Barcode Number"].isin(selected_brnumber)]


    csv_data = dt.to_csv(index=False).encode('utf-8-sig')

    st.download_button(label="📥 Download Analysis Data",
                       data= csv_data,
                       file_name="log_analysis.csv",
                       mime="text/csv")

    st.dataframe(dt, use_container_width=True)

else:
    st.info("Please upload log files from the left side for analysis.")