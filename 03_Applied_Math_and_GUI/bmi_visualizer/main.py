import math
from tkinter import *


window = Tk()
window.title("BMI Calculator")
window.minsize(400,400)
window.config(padx=10, pady=10)


def calculate_bmi():
    try:
        canvas.delete("needle")
        height_str = entry1.get()
        weight_str = entry2.get()
        height_num = float(height_str)
        weight_num = float(weight_str)
        height_m = height_num / 100
        bmi_resulth = weight_num / height_m ** 2

        bmi_for_angle = bmi_resulth

        if bmi_for_angle > 40:
            bmi_for_angle = 40
        elif bmi_for_angle < 10:
            bmi_for_angle = 10

        if bmi_resulth < 14.0:
            persentage = (bmi_for_angle - 10) / (14 - 10)
            bmi_angle = 0 + (persentage * (36 - 0))
            category_str = "You are Very Weak person 😮"
        elif bmi_resulth < 18.8:
            persentage = (bmi_for_angle - 14) / (18.8 - 14)
            bmi_angle = 36 + (persentage * (72 - 36))
            category_str = "You are Weak person 😟"
        elif bmi_resulth < 24.9:
            persentage = (bmi_for_angle - 18.8) / (24.9 - 18.8)
            bmi_angle = 72 + (persentage * (108 - 72))
            category_str = "You are Normal person! 😊"
        elif bmi_resulth < 29.9:
            persentage = (bmi_for_angle - 24.9) / (29.9 - 24.9)
            bmi_angle =  108 + (persentage *(144-108))
            category_str = "You are Overweight person! 😐"
        else:
            persentage = (bmi_for_angle - 29.9) / (40 - 29.9)
            bmi_angle = 144 + (persentage * (180 - 144))
            category_str = "You are Obese Person! 😮"

        x2 = 150 + (120 * math.cos(math.radians(bmi_angle)))
        y2 = 140 - (120 * math.sin(math.radians(bmi_angle)))

        line = canvas.create_line(150, 140, x2, y2, width=3, fill="black", tags="needle", arrow="last")
        resulth_label.config(text= f"Your BMI score : {bmi_resulth:.1f}, BMI Catagories : {category_str}")

    except ValueError:
        resulth_label.config(text="Please enter only numbers!")


label1 = Label(window, text="Height:")
label1.pack()

entry1 = Entry(window, width=20)
entry1.pack()

label2 = Label(window, text="Weight:")
label2.pack()

entry2 = Entry(window, width=20)
entry2.pack()

button = Button(window, text="Click for calculate!", command=calculate_bmi)
button.pack()

resulth_label = Label(window, text="")
resulth_label.pack()

canvas = Canvas(width=300, height=150)
canvas.create_arc(20,10, 280, 270, start=0, extent=36, style="arc", outline="red", width=10)
canvas.create_arc(20,10, 280, 270, start=36, extent=36, style="arc", outline="orange", width=10)
canvas.create_arc(20,10, 280, 270, start=72, extent=36, style="arc", outline="green", width=10)
canvas.create_arc(20,10, 280, 270, start=108, extent=36, style="arc", outline="orange", width=10)
canvas.create_arc(20,10, 280, 270, start=144, extent=36, style="arc", outline="red", width=10)


canvas.create_text(150, 35, text="Normal")
canvas.create_text(212, 55, text="Underweight")
canvas.create_text(88, 55, text="Overweight")
canvas.create_text(250, 108, text="Severely Underweight")
canvas.create_text(50, 108, text="Obese")

canvas.pack()

window.mainloop()

