import tkinter as tk
from tkinter import ttk
##from productos_reactivos import Productos
from tkinter import messagebox
import json
from just_the_module import Save_module
class Color_selector:
    def __init__(self,root):
        def update_color(value):
            # Update the color based on the slider value
            red = int(red_slider.get())
            green = int(green_slider.get())
            blue = int(blue_slider.get())
            color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
            color_label.config(bg=color)
            
            # Update the color rectangle
            color_rectangle.config(bg=color)
        color_window = tk.Toplevel(root)# 0
        color_window.title("Crear Metodo de Fabricación Estandar")
        # Create sliders for Red, Green, and Blue
        red_label = ttk.Label(color_window, text="Red:")
        red_label.grid(row=0, column=0, padx=10, pady=5)
        red_slider = ttk.Scale(color_window, from_=0, to=255, orient="horizontal", command=update_color)
        red_slider.grid(row=0, column=1, padx=10, pady=5)

        green_label = ttk.Label(color_window, text="Green:")
        green_label.grid(row=1, column=0, padx=10, pady=5)
        green_slider = ttk.Scale(color_window, from_=0, to=255, orient="horizontal", command=update_color)
        green_slider.grid(row=1, column=1, padx=10, pady=5)

        blue_label = ttk.Label(color_window, text="Blue:")
        blue_label.grid(row=2, column=0, padx=10, pady=5)
        blue_slider = ttk.Scale(color_window, from_=0, to=255, orient="horizontal", command=update_color)
        blue_slider.grid(row=2, column=1, padx=10, pady=5)

        # Create a label to display the selected color
        color_label = ttk.Label(color_window, text="Selected Color", width=20, height=3)
        color_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a rectangle to display the selected color
        color_rectangle = ttk.Label(color_window, text="", width=10, height=2)
        color_rectangle.grid(row=4, column=0, columnspan=2, pady=10)
