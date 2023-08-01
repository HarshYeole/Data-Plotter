import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

#enter = (input("Enter file:\n"))
count = 0
def draw_graph(num):
    
    data = pd.read_csv("C:/Users/yeole/OneDrive/Desktop/BARC/Trainees/Home/T05_LU_2022(OG).txt",names = ["Index","Time","Area1","Area2","Area3","Area4"],index_col = 0)
    data1 =(data.Time)
    data2 =(data.Area1)
    A = []
    B = []
    global count
    count = count + 1
    A.append(data["Time"][count])
    B.append(data["Area1"][count])
    x_axis = len(data1)
    plt.cla()
    plt.plot(A, B)
    plt.xticks([x for x in range(0,x_axis,int(x_axis/9))])
    plt.grid()

anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval = 0)
plt.show()
