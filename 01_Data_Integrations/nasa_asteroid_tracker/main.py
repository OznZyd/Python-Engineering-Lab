import webbrowser

import requests
from tkinter import *
from tkinter import messagebox
import threading

# --UI Setup--
window = Tk()
window.config(padx=10, pady=10, bg="black")
window.geometry("500x550")
window.title("Dangerous asteroids approaching Earth!")

photo_image = PhotoImage(file="astreoid_image.png")

logo_label = Label(window, image= photo_image, width=500, height=200)
logo_label.pack()

logo_label.image = photo_image

# Lists to manage data ant UI elemnts
dangerous_asteroids = []
result_widgets = []
trash_box = []

for trash2 in trash_box:
    trash2.destroy()

result_widgets.clear()
# --UI Elements--
title_label = Label(window, text="Dangerous asteroids approaching Earth!", bg="black", fg="white", font=("Verdana", 20, "bold"), padx=5, pady=5)
title_label.pack()
result_widgets.append(title_label)

label4 = Label(window, text="Enter Date(YYYY-MM-DD)", bg="black", fg= "white", font=("Arial", 13, "italic"), padx=5, pady=5)
label4.pack()

date_input = Entry(window)
date_input.pack()

# -- Functions --
def start_thread():
    """Starts the data fetching process in a separate thread to prevent UI freezing."""
    worker = threading.Thread(target=check_asteroids)
    worker.start()


def check_asteroids():
    """Fetches data from NASA, filters hazardous asteroids, and updates the UI."""

    # 1. Clean up previous results from the screen
    dangerous_asteroids.clear()
    for trash in result_widgets:
        trash.destroy()

    result_widgets.clear()

    # 2. Prepare API request
    # NOTE: Using DEMO_KEY for public sharing. For production, use environment variables.
    nasa_url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {"api_key": "DEMO_KEY","start_date": date_input.get()}

    # 3. Fetch Data with Error Handling
    try:
        response = requests.get(nasa_url, params=params)
        data = response.json()
        date = date_input.get()
        today_data = data["near_earth_objects"][date]
        print(today_data[0]["close_approach_data"][0])
    except KeyError:
        messagebox.showerror(title="Error", message="Please enter the date information in the valid form!")
        return

     # 4. Filter Data
    dangerous_asteroids.clear()
    for index, line in enumerate(today_data):
        if line["is_potentially_hazardous_asteroid"] == True:
            dangerous_asteroids.append(line)

    # 5. Update UI
    if not dangerous_asteroids:
        # If no dangerous asteroids found, show a safe message
        safe_label = Label(window, text="No threats detected for this date! 🌍🛡️", bg="black", fg="#00FF00", font=("Arial", 20, "bold"))
        safe_label.pack(pady = 20)
        result_widgets.append(safe_label)

    else:
        asteroid_count = len(dangerous_asteroids)
        astroid_count_label = Label(window, text=f"🚨 WARNING: {asteroid_count} THREATS DETECTED! 🚨", bg="black", fg="#FFFF00", font=("Verdana", 14, "bold"))
        astroid_count_label.pack()
        result_widgets.append(astroid_count_label)

        for ast in dangerous_asteroids:

            link = ast["nasa_jpl_url"]

            speed_value = float(ast["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])
            # Create labels for each asteroid
            name_label = Label(window, text=f"⚠️Asteroid name: {ast['name']}", bg="black", fg="#FF4500", font=("Arial", 15, "bold"), cursor="hand2")
            name_label.pack()
            name_label.bind("<Button-1>", lambda e: webbrowser.open(link))
            result_widgets.append(name_label)

            speed_label = Label(window, text=f"🚀Asteroid Speed: {speed_value:.2f} km/sa", bg="black", fg="white",font=("Arial", 15, "bold"))
            speed_label.pack()
            result_widgets.append(speed_label)

            distance_value = float(ast["close_approach_data"][0]["miss_distance"]["kilometers"])
            distance_label = Label(window, text=f"📏 Distance to Earth: {distance_value:.2f} km", bg="black", fg="white", font=("Arial", 15, "bold"))
            distance_label.pack()
            result_widgets.append(distance_label)

# -- Start Button --
button1 = Button(window, text="Start", command=start_thread, pady=5, padx=5)
button1.pack()



window.mainloop()