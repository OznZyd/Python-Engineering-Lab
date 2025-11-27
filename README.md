# 🧪 Python Engineering Lab

> **"Turning logic into functional tools."**

This repository documents my transition from **Industrial Engineering** to **Software Development & Data Analysis**. It contains practical implementations of algorithms, data fetching pipelines, security protocols, and mathematical visualizations.

**Current Focus:** Building robust, data-driven applications while mastering Python's ecosystem.

---

## 📂 Project Modules

### 1. Data Integrations & API Handling
*Real-world data fetching, parsing, and asynchronous processing.*

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

---

## 🛠 Tech Stack & Tools
* **Languages:** Python 3.x
* **Libraries:** Pandas (Learning), Requests, Tkinter, Turtle, Cryptography.
* **Core Concepts:** OOP, Multithreading, JSON Parsing, REST APIs, Data Security.


## 👨‍💻 Author
**Ozan Zeydanoglu** - *Engineering Professional & Developer*
*Bridging engineering discipline with Software Development. Open to professional challenges in Engineering IT, Automation, and Data Solutions.*
