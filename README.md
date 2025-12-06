# 🧪 Python Engineering Lab

> **"Turning logic into functional tools."**

This repository demonstrates the application of **Engineering Principles** to **Software Development & Data Analysis**. It features practical implementations of algorithms, automated data pipelines, security protocols, and mathematical visualizations.

**Current Focus:** Building robust, data-driven applications while mastering Python's ecosystem.

---

## 📂 Project Modules

### 1. Data Integrations & API Handling
*Real-world data fetching, parsing, and asynchronous processing.*

* **📊 Automated Sales Reporter:**
    * **What it does:** An ETL pipeline that processes raw Excel sales data, calculates financial metrics, and generates visual reports.
    * **Engineering approach:** Features **Logging mechanism** for process monitoring, modular function design, and error handling.
    * **Tech:** `Pandas`, `Matplotlib`, `Logging`.
    
* **🪐 Orbital Sentry (NASA API):**
    * **What it does:** Fetches real-time Near-Earth Object (NEO) data from NASA, filters hazardous asteroids, and visualizes threats.
    * **Engineering approach:** Implemented **Multithreading** to prevent UI freezing during API calls. Uses structured Exception Handling for network reliability.
    * **Tech:** `requests`, `threading`, `json`, `Tkinter`.
    
* **Weather CLI Tool:**
    * **What it does:** A command-line interface tool that queries weather APIs and parses JSON responses for specific cities.
    * **Tech:** `requests`, `CLI interaction`.

### 2. Security & Data Persistence
*Understanding data privacy, hashing, and file I/O operations.*

* **🔐 Secure Notes Manager:**
    * **What it does:** A desktop tool to encrypt and decrypt sensitive local files using a master key.
    * **Engineering approach:** Utilizes **SHA-256 Hashing** for password verification and **Fernet (Symmetric Encryption)** for data protection. No raw passwords are stored.
    * **Tech:** `cryptography`, `hashlib`, `base64`.

### 3. Applied Math & Visualization
*Mathematical modeling and event-driven logic.*

* **Health Metrics Visualizer (BMI):**
    * **What it does:** Calculates body mass metrics and visualizes the result on a dynamic gauge.
    * **Engineering approach:** Used Trigonometry (`sin`/`cos`) to map numerical data to geometric angles for the speedometer needle animation.
* **Event-Driven Simulation (Turtle):**
    * **What it does:** An interactive reflex simulation.
    * **Engineering approach:** Manages recursive timer loops and event listeners (`onclick`) to handle real-time state changes.

### 4. Interactive Data Apps (Streamlit)
*Full-stack data applications with web interfaces and secure logic.*

* **🕵️‍♂️ OpsTrace Analytics:**
    * **What it does:** An industrial-grade log analysis platform that merges, cleans, and visualizes scattered log files. Features a secure login system and advanced time-series filtering.
    * **Engineering approach:** Implemented **Session State** for security, **Multi-file ETL pipeline** with `pd.concat`, and **Chained Filtering Logic** for drill-down analysis.
    * **Tech:** `Streamlit`, `Pandas`, `Datetime`, `SessionState`.

---

## 🛠 Tech Stack & Tools
* **Languages:** Python 3.x
* **Libraries:** Pandas (Learning), Requests, Tkinter, Turtle, Cryptography, Streamlit.
* **Core Concepts:** OOP, Multithreading, JSON Parsing, REST APIs, Data Security, ETL Pipelines.


## 👨‍💻 Author
**Ozan Zeydanoglu** - *Engineering Professional & Developer*
*Bridging engineering discipline with Software Development. Open to professional challenges in Engineering IT, Automation, and Data Solutions.*
