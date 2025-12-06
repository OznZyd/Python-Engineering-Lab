# 🕵️‍♂️ OpsTrace Analytics

> **"Turning raw industrial logs into actionable insights."**

**OpsTrace Analytics** is a professional-grade log analysis tool designed to help engineers visualize, filter, and extract meaningful data from scattered log files. It transforms manual, time-consuming error tracing into a few clicks.

![OpsTrace UI](assets/dashboard_header.png)

## 🎯 Key Features (v2.0)

* **🔐 Secure Access:** Session-state based login system to protect operational data.
* **📂 Multi-File Ingestion:** Drag & drop interface to merge multiple log files (.log, .txt) into a single master dataset automatically.
* **🧠 Intelligent Parsing:** Handles "ragged" data structures (variable column lengths) dynamically without data loss.
* **⏳ Time Machine Filtering:** Precise date & time range filtering with UTC timezone normalization.
* **🔗 Chained Filtering Logic:** Dynamic dropdowns where Sub-Category depends on Category, and Zone depends on Sub-Category.
* **📥 One-Click Export:** Generates Windows-compatible (UTF-8-SIG) CSV reports for management.

## 🛠 Tech Stack & Concepts Used

* **Core:** Python 3.x
* **Data Engine:** `Pandas` (ETL, Concat, Filtering, DateTime Conversion)
* **Interface:** `Streamlit` (Session State, Forms, Sidebar Layout)
* **Engineering Patterns:**
    * **ETL Pipeline:** Extract (Load), Transform (Clean/Merge), Load (Display).
    * **Session State Management:** Handling persistent login status across re-runs.
    * **Timezone Handling:** `dt.tz_localize(None)` for robust time comparisons.
    * **Defensive Coding:** `try-except` blocks and `len()` checks to prevent crashes.

## 🚀 How to Run

1.  **Windows (Easy Mode):** Double click `Baslat.bat` (or the desktop shortcut).
2.  **Manual Mode:**
    ```bash
    streamlit run app.py
    ```
3.  **Login Credentials:**
    * **Password:** `31082024`

---
*Developed by Ozan Zeydanoglu - Engineering Professional*