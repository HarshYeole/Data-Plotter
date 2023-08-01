import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/yeole/OneDrive/Desktop/BARC/Trainees/T05_LU_2022-09-27 142643.113726.txt", names=["Time", "Area1", "Area2", "Area3", "Area4"], index_col=0)

data1 = data["Time"]
data2 = data["Area1"]
count = 0
length = len(data1) - 1
A = []
B = []

def draw_graph(num_points):
    global count
    for _ in range(num_points):
        count += 1
        A.append(data1[count])
        B.append(data2[count])
    x_axis = len(data1)
    plt.cla()
    plt.plot(A, B)
    plt.xticks([x for x in range(0, x_axis, int(x_axis/9))])
    plt.grid()

draw_graph(length)
plt.show()