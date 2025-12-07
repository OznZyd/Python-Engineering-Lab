# 🕵️‍♂️ OpsTrace Analytics

> **"Turning raw industrial logs into actionable insights."**

**OpsTrace Analytics** is a professional-grade log analysis tool designed to help engineers visualize, filter, and extract meaningful data from scattered log files. It transforms manual, time-consuming error tracing into a few clicks.

![OpsTrace UI](assets/dashboard_header.png)

## 🚀 Release Notes (v2.0 - Final)

This version introduces significant performance improvements and deployment features over v1.5:

* **⚡ Performance Boost:** Implemented `@st.cache_data` for instant CSV conversion and file loading. Replaced pagination with **AgGrid Virtualization** to handle 100k+ rows without lag.
* **🔍 Global Error Hunter:** New search capability to scan the entire dataset for specific keywords like "Error", "Fail", or "Exception" across all columns instantly.
* **🧠 Logic Upgrade:** "Divert Status" filter upgraded to **Inclusion Logic** (Check-to-see), preventing data loss during filtering.
* **📦 Windows Deployment:** Added `.bat` scripts and icon configuration for one-click execution on Windows environments without IDE requirement.
* **🎨 UI Polish:** Enhanced visual hierarchy, removed top padding, and added a custom "Welcome" screen.

## 🎯 Key Features

* **🔐 Secure Access:** Session-state based login system to protect operational data.
* **📂 Multi-File Ingestion:** Drag & drop interface to merge multiple log files (.log, .txt) into a single master dataset automatically.
* **⏳ Time Machine Filtering:** Precise date & time range filtering with UTC timezone normalization.
* **🔗 Chained Filtering Logic:** Dynamic dropdowns where Sub-Category depends on Category, and Zone depends on Sub-Category.
* **📥 One-Click Export:** Generates Windows-compatible (UTF-8-SIG) CSV reports for management.

## 🛠 Tech Stack & Concepts Used

* **Core:** Python 3.x
* **Data Engine:** `Pandas` (ETL, Concat, Filtering, DateTime Conversion)
* **Interface:** `Streamlit`, `AgGrid` (Advanced Tables)
* **Engineering Patterns:**
    * **ETL Pipeline:** Extract (Load), Transform (Clean/Merge), Load (Display).
    * **Caching Strategy:** Optimization for heavy I/O operations.
    * **Defensive Coding:** `try-except` blocks and `len()` checks to prevent crashes.

## 🚀 How to Run

1.  **Windows (Easy Mode):** Double click `Baslat.bat` (or the desktop shortcut).
2.  **Manual Mode:**
    ```bash
    streamlit run app.py
    ```
3.  **Login Credentials:**
    * **Password:** `******`

---
*Developed by Ozan Zeydanoglu *
