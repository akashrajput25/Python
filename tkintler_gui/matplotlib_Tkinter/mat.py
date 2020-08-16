from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Graphs')
root.geometry('400x500')

def graph():
    house_prices = np.random.normal(200000,13000,1000)
    plt.polar(house_prices )
    plt.show()

my_btn = Button(root ,text="graph" , command = graph)
my_btn.pack()

root.mainloop()