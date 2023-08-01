import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Create some sample data
t = np.linspace(0, 10, 1000)
y = np.sin(t)

# Create a figure and axis
fig, ax = plt.subplots()
ax.plot(t, y)

# Create a function to zoom in the plot
def zoom_in():
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Calculate the center point of the plot
    x_center = (xlim[1] + xlim[0]) / 2
    y_center = (ylim[1] + ylim[0]) / 2
    
    # Calculate the new width and height of the plot
    new_width = (xlim[1] - xlim[0]) / 1.5
    new_height = (ylim[1] - ylim[0]) / 1.5
    
    # Calculate the new limits based on the center point
    new_xlim = x_center - new_width / 2, x_center + new_width / 2
    new_ylim = y_center - new_height / 2, y_center + new_height / 2
    
    ax.set_xlim(new_xlim)
    ax.set_ylim(new_ylim)
    canvas.draw_idle()

# Create a function to zoom out the plot
def zoom_out():
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Calculate the center point of the plot
    x_center = (xlim[1] + xlim[0]) / 2
    y_center = (ylim[1] + ylim[0]) / 2
    
    # Calculate the new width and height of the plot
    new_width = (xlim[1] - xlim[0]) * 1.5
    new_height = (ylim[1] - ylim[0]) * 1.5
    
    # Calculate the new limits based on the center point
    new_xlim = x_center - new_width / 2, x_center + new_width / 2
    new_ylim = y_center - new_height / 2, y_center + new_height / 2
    
    ax.set_xlim(new_xlim)
    ax.set_ylim(new_ylim)
    canvas.draw_idle()

# Create the GUI window and add the figure to it
root = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Create the zoom in and zoom out buttons
zoom_in_button = tk.Button(master=root, text="Zoom In", command=zoom_in)
zoom_in_button.pack(side=tk.LEFT)
zoom_out_button = tk.Button(master=root, text="Zoom Out", command=zoom_out)
zoom_out_button.pack(side=tk.LEFT)

# Start the GUI mainloop
tk.mainloop()
