# 🪐 Orbital Sentry - NASA NEO Tracker

An asteroid tracking application built with **Python**, utilizing the **NASA API** to fetch real-time data about Near-Earth Objects (NEOs).

![Project Status](https://img.shields.io/badge/Status-Active-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)

## 🚀 About The Project

This application serves as a desktop radar for hazardous asteroids. It fetches data from NASA's servers asynchronously to ensure a smooth user experience without freezing the interface.

**Key Features:**
* **Live Data:** Connects to NASA's NeoWs (Near Earth Object Web Service) API.
* **Responsive UI:** Built with `Tkinter` for a clean, dark-mode dashboard.
* **High Performance:** Implements **Multithreading** to separate API requests from the UI loop.
* **Error Handling:** Robust protection against invalid inputs and connection issues.

## 👨‍💻 Author's Note

> "This project was developed during my transition from engineering to software development to grasp the core concepts of **API integration**, **GUI design**, and **asynchronous programming** logic."

## 🛠️ Built With

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Requests Library](https://pypi.org/project/requests/)
* NASA API

## 🏁 How to Run

1.  Clone the repo:
    ```sh
    git clone [https://github.com/OznZyd/Orbital-Sentry.git](https://github.com/OznZyd/Orbital-Sentry.git)
    ```
2.  Install requests:
    ```sh
    pip install requests
    ```
3.  Run the application:
    ```sh
    python main.py
    ```

---
*Created by ["Ozan Zeydanoglu"]*