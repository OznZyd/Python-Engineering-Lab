import pandas as pd
import streamlit as st
import main
from datetime import datetime, time
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


st.set_page_config(layout="wide", page_title="OpsTrace Analytics")


st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def local_all_data(files):
    all_files = []
    for file in files:
        data = main.load_data(file)
        all_files.append(data)

    dt = pd.concat(all_files)
    dt = dt.dropna(axis=1, how='all')

    dt["Time"] = dt["Time"].astype(str).str.strip()
    dt["Time"] = pd.to_datetime(dt["Time"], errors='coerce', utc=True)

    for clm in dt.columns:
        if dt[clm].dtype == 'object':
            dt[clm] = dt[clm].astype(str)

    return dt


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8-sig')



if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("")

    st.image("assets/Welcome_Screen.png", use_container_width=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("login_form"):
            password = st.text_input("🔑 Enter Access Key", type="password", placeholder="••••••••")
            submit_button = st.form_submit_button("🔓 Login", use_container_width=True)

    if submit_button:
        if password == "31082024":
            st.session_state.logged_in = True
            st.rerun()
        else:
            col2.error("Wrong Password!")
    st.stop()


st.image("assets/Main_Screen.png", use_container_width=True)
st.sidebar.image("assets/SideBar.png", width=300)

st.sidebar.markdown("""
    <h2 style='text-align: left; color: black; font-family: monospace;'>
        🕵️‍♂️ FILTERS
    </h2>
    """,
                    unsafe_allow_html=True)


update_files = st.sidebar.file_uploader("Update .log Files", accept_multiple_files=True)

if update_files:
    dt = local_all_data(update_files)


    selected_cat = []
    selected_subct = []
    selected_zone = []
    selected_mc = []
    selected_pcknumber = []
    selected_description = []
    selected_brnumber = []
    selected_statuses = []


    with st.sidebar.form("filter_form"):
        min_date = dt["Time"].min()
        max_date = dt["Time"].max()

        selected_dates = st.date_input("Select Date Range", [min_date, max_date])

        co11, co12 = st.columns(2)
        with co11:
            start_time = st.time_input("Start Time", value=time(0, 0))
        with co12:
            end_time = st.time_input("End Time", value=time(23, 59))

        st.markdown("---")
        st.markdown("**🚨 Global Error Hunter**")
        show_only_errors = st.checkbox("Show rows containing 'Error'", value=False)
        st.markdown("---")

        if "Category" in dt.columns:
            dt["Category"] = dt["Category"].str.strip()
            dc = dt["Category"].unique().tolist()
            selected_cat = st.multiselect("Selected Category", dc)

        if "SubCategory" in dt.columns:
            dt["SubCategory"] = dt["SubCategory"].str.strip()
            ds = dt["SubCategory"].unique().tolist()
            selected_subct = st.multiselect("Selected Sub-Category", ds)

        if "Zone" in dt.columns:
            dt["Zone"] = dt["Zone"].str.strip()
            dz = dt["Zone"].unique().tolist()
            selected_zone = st.multiselect("Selected Zone", dz)

        if "Marc Code" in dt.columns:
            dt["Marc Code"] = dt["Marc Code"].astype(str).str.strip()
            dm = dt["Marc Code"].unique().tolist()
            selected_mc = st.multiselect("Selected Marc Code", dm)

        if "Pick Number" in dt.columns:
            dp = dt["Pick Number"].unique().tolist()
            selected_pcknumber = st.multiselect("Selected PickNumber", dp)

        if "Description_1" in dt.columns:
            dt["Description_1"] = dt["Description_1"].astype(str).str.strip()
            dd = dt["Description_1"].unique().tolist()
            selected_description = st.multiselect("Selected Description", dd)

        if "Barcode Number" in dt.columns:
            dt["Barcode Number"] = dt["Barcode Number"].astype(str).str.strip()
            db = dt["Barcode Number"].unique().tolist()
            selected_brnumber = st.multiselect("Selected Barcode Number", db)


        if "Divert Status" in dt.columns:
            dt["Divert Status"] = dt["Divert Status"].astype(str).str.strip()
            st.markdown("---")
            st.markdown("**🚦 Divert Status**")


            target_keywords = ['Success', 'Failed', 'Fail']
            all_statuses = dt["Divert Status"].unique().tolist()


            present_targets = [x for x in all_statuses if x in target_keywords]

            if len(present_targets) > 0:
                cols = st.columns(len(present_targets))
                for i, status in enumerate(present_targets):
                    with cols[i]:

                        is_checked = st.checkbox(status, value=False, key=f"chk_{status}")
                        if is_checked:
                            selected_statuses.append(status)

        st.markdown("<br>", unsafe_allow_html=True)

        apply_button = st.form_submit_button("✅ APPLY FILTERS", use_container_width=True)




    if len(selected_dates) == 2:
        dt["Time"] = dt["Time"].dt.tz_localize(None)
        start_date = selected_dates[0]
        end_date = selected_dates[1]
        all_start = datetime.combine(start_date, start_time)
        all_end = datetime.combine(end_date, end_time)
        dt = dt[(dt["Time"] >= all_start) & (dt["Time"] <= all_end)]

    if show_only_errors:
        mask = dt.astype(str).apply(lambda x:x.str.contains('Error', case=False, na=False)).any(axis=1)
        dt = dt[mask]


    if selected_cat:
        dt = dt[dt["Category"].isin(selected_cat)]
    if selected_subct:
        dt = dt[dt["SubCategory"].isin(selected_subct)]
    if selected_zone:
        dt = dt[dt["Zone"].isin(selected_zone)]
    if selected_mc:
        dt = dt[dt["Marc Code"].isin(selected_mc)]
    if selected_pcknumber:
        dt = dt[dt["Pick Number"].isin(selected_pcknumber)]
    if selected_description:
        dt = dt[dt["Description_1"].isin(selected_description)]
    if selected_brnumber:
        dt = dt[dt["Barcode Number"].isin(selected_brnumber)]


    if selected_statuses:
        dt = dt[dt["Divert Status"].isin(selected_statuses)]


    csv_data = convert_df(dt)

    st.download_button(
        label="📥 Download Analysis Data (CSV)",
        data=csv_data,
        file_name="log_analysis.csv",
        mime="text/csv",
    )

    display_limit = 20000
    st.info(f"Displaying top {display_limit} rows of {len(dt)} results. Download CSV for full data.")


    builder = GridOptionsBuilder.from_dataframe(dt.head(display_limit))
    builder.configure_default_column(
        groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True,
        filter=True, sortable=True, minWidth=150, floatingFilter=True
    )
    builder.configure_side_bar()
    grid_options = builder.build()

    AgGrid(
        dt.head(display_limit),
        gridOptions=grid_options,
        height=800,
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=False,
        update_mode=GridUpdateMode.NO_UPDATE,
        allow_unsafe_jscode=True
    )

else:
    st.info("Please upload log files from the left sidebar to begin analysis.")