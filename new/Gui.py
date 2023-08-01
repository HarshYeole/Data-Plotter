import matplotlib.pyplot as plt

# Given data
data = [
    [0, '14:26:43', 0.16982765981681708, 0.09288986391869877, 0.17076630565919038, 0.09419405462529999],
    [1, '14:26:46', 0.15012782530150384, 0.08396132387470004, 0.15220215314126348, 0.08755824304872677],
    [2, '14:26:49', 0.1571297243584788, 0.08750101751163626, 0.1520036443296867, 0.08697494530191198],
    [3, '14:26:51', 0.17786227221202605, 0.09861634178434034, 0.1713089031575785, 0.09781492733964704],
    [4, '14:26:54', 0.15354516040658583, 0.08776334444235565, 0.1589951997480008, 0.09127300718631616],
    [5, '14:26:56', 0.1832217868195244, 0.10243710003879376, 0.18794525595044992, 0.10598601059555067],
    [6, '14:26:59', 0.16748056996886668, 0.09515904312988313, 0.16390777411702342, 0.09503122200281383],
    [7, '14:27:02', 0.17116600252645145, 0.09730571933442299, 0.1743227067596305, 0.10236787217627302],
    [8, '14:27:04', 0.1600598022423267, 0.09158516628595549, 0.15785620262078012, 0.09398186314553038],
    [9, '14:27:07', 0.15864257651304833, 0.09401483143928943, 0.15953633812842413, 0.09797070325184633],
    [10, '14:27:09', 0.1701415888402707, 0.10089757470737704, 0.17095454769017426, 0.10207799557596466],
    [11, '14:27:12', 0.1535234845362276, 0.0915885594546097, 0.15352196949860972, 0.09464983540913088],
    [12, '14:27:14', 0.14594607931625977, 0.08785804511725424, 0.15611190658620994, 0.09454627170963213],
    [13, '14:27:17', 0.14763617500282544, 0.08916345171555864, 0.14797021413175324, 0.09256114419347129],
    [14, '14:27:19', 0.1538461765478152, 0.09383469690750348, 0.15652181611536967, 0.09764968202589078],
    [15, '14:27:22', 0.15422925475586166, 0.09537184238033365, 0.15559696056519473, 0.09864875301893329],
    [16, '14:27:24', 0.1596370285163073, 0.09731741797211584, 0.15375862831857462, 0.09834955838029268],
    [17, '14:27:27', 0.17666575433888035, 0.1066523620294642, 0.1736162443900039, 0.10935711597951617],
    [18, '14:27:30', 0.15802333481033295, 0.0987812333465437, 0.15614683709944768, 0.10304647901302666],
    [19, '14:27:32', 0.1566170692221746, 0.09660558958186291, 0.1554705856397031, 0.10044630101006463],
    [20, '14:27:35', 0.1273086116010398, 0.08422344821853346, 0.12633616571252723, 0.08747286041931955]
]

# Extract x and y values from data
x = [row[0] for row in data]
y1 = [row[2] for row in data]
y2 = [row[4] for row in data]

# Plot the data
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Y1')
line2, = ax.plot(x, y2, label='Y2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Data Plot')
ax.legend()

# Variables to store the zoomed data
zoomed_data = []

# Function to handle zoom in
def zoom_in(event):
    ax.set_xlim(event.xdata - 1, event.xdata + 1)  # Zoom in on X-axis
    ax.set_ylim(event.ydata - 0.1, event.ydata + 0.1)  # Zoom in on Y-axis
    update_zoomed_data()
    plt.draw()

# Function to handle zoom out
def zoom_out(event):
    ax.set_xlim(0, 20)  # Reset X-axis limits
    ax.set_ylim(0.08, 0.19)  # Reset Y-axis limits
    update_zoomed_data()
    plt.draw()

# Function to update the zoomed data
def update_zoomed_data():
    global zoomed_data
    zoomed_data = []
    for i in range(len(x)):
        if x[i] >= ax.get_xlim()[0] and x[i] <= ax.get_xlim()[1] and y1[i] >= ax.get_ylim()[0] and y1[i] <= ax.get_ylim()[1]:
            zoomed_data.append([x[i], data[i][1], y1[i], data[i][3], y2[i], data[i][5]])

# Function to handle screenshot
def save_screenshot():
    with open('zoomed_data.txt', 'w') as f:
        for row in zoomed_data:
            f.write(','.join([str(value) for value in row]) + '\n')
    print('Screenshot saved as zoomed_data.txt')

# Create zoom in button
zoom_in_button = plt.axes([0.71, 0.05, 0.1, 0.04])
button1 = plt.Button(zoom_in_button, 'Zoom In')
button1.on_clicked(zoom_in)

# Create zoom out button
zoom_out_button = plt.axes([0.81, 0.05, 0.1, 0.04])
button2 = plt.Button(zoom_out_button, 'Zoom Out')
button2.on_clicked(zoom_out)

# Create screenshot button
screenshot_button = plt.axes([0.91, 0.05, 0.1, 0.04])
button3 = plt.Button(screenshot_button, 'Screenshot')
button3.on_clicked(save_screenshot)

# Show the plot
plt.show()
