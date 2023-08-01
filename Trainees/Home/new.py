import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from PIL import ImageTk, Image

data = pd.read_csv("C:/Users/yeole/OneDrive/Desktop/BARC/Trainees/T05_LU_2022-09-27 142643.113726.txt", names=["Time", "Area1", "Area2", "Area3", "Area4"], index_col=0)

data1 = data["Time"]
data2 = data["Area1"]
count = 0
A = []
B = []

fig, ax = plt.subplots(figsize=(10, 6))  # Larger window size

def draw_live_graph():
    global count
    count += 1
    A.append(data1[count])
    B.append(data2[count])
    x_axis = len(data1)
    ax.cla()
    ax.plot(A, B)
    ax.set_xticks([x for x in range(0, x_axis, int(x_axis/9))])
    ax.grid()
    canvas.draw()

def take_screenshot():
    screenshot = ax.figure.canvas.copy_from_bbox(ax.bbox)
    plt.tight_layout()
    canvas.draw()
    
    # Save the screenshot as an image file
    screenshot_path = "screenshot.png"
    fig.savefig(screenshot_path)
    open_screenshot_window(screenshot_path, A, B)

def open_screenshot_window(screenshot_path, A, B):
    # Create a new window for the screenshot
    screenshot_window = tk.Toplevel(root)
    screenshot_window.title("Screenshot")

    # Create a new figure and plot the data
    fig_screenshot, ax_screenshot = plt.subplots(figsize=(8, 6))
    ax_screenshot.plot(A, B)
    ax_screenshot.set_xlabel("Time")
    ax_screenshot.set_ylabel("Area1")
    ax_screenshot.grid()

    #zoom in
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
        canvas_screenshot.draw_idle()

    #zoom out
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
        canvas_screenshot.draw_idle()

    # Create the zoom in and zoom out buttons
    zoom_in_button = tk.Button(master=screenshot_window, text="Zoom In", command=zoom_in)
    zoom_in_button.pack(side=tk.RIGHT)
    zoom_out_button = tk.Button(master=screenshot_window, text="Zoom Out", command=zoom_out)
    zoom_out_button.pack(side=tk.RIGHT)

    # Load the screenshot image
    screenshot_image = ImageTk.PhotoImage(Image.open(screenshot_path))

    # Create a label to display the screenshot image
    screenshot_label = tk.Label(screenshot_window, image=screenshot_image)
    screenshot_label.pack(side=tk.LEFT)

    # Create a canvas for the screenshot plot
    canvas_screenshot = FigureCanvasTkAgg(fig_screenshot, master=screenshot_window)
    canvas_screenshot.draw()

    # Set the window size based on the image size and plot size
    screenshot_window.geometry(f"{screenshot_image.width() + fig_screenshot.get_figwidth()*100}x{max(screenshot_image.height(), fig_screenshot.get_figheight()*100)}")

    # Update the window to display the image and plot
    screenshot_window.update()

# Create the GUI window
root = tk.Tk()
root.geometry("800x600")  # Set the main window size

# Create a figure canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill the entire window with the graph

# Create the "Take Screenshot" button
screenshot_button = tk.Button(master=root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(side=tk.BOTTOM)  # Position the button at the bottom of the window

def update_graph():
    draw_live_graph()
    root.after(10, update_graph)  # Update every 10 milliseconds

# Start the live data update process
update_graph()

# Start the GUI mainloop
tk.mainloop()