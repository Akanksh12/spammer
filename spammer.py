from time import sleep
from pynput.keyboard import Key, Controller
import tkinter as tk
from tkinter import *

k = Controller()

window = tk.Tk()
window.geometry("300x150")

wel = tk.Label(text="Welcome to spammer.exe!", width=100, height=1)
wel.pack()

pl = tk.Label(text="Your phrase", width=100, height=1)
pl.pack()

st = tk.Entry(text="your phrase")
st.pack()

dl = tk.Label(text="Delay(s)", width=100, height=1)
dl.pack()

d = tk.Entry(text="delay")
d.pack()

def button():
    dela = d.get()
    string = st.get()
    if dela == '':
        dela = 0
    delay = float(dela)
    if delay == '':
        delay = 0
        
    sleep(5)
    while(1 > 0):
        sleep(delay)
        k.type(string)
        k.press(Key.enter)
        k.release(Key.enter)

b = tk.Button(text="execute in 5 sec",command=button)
b.pack()

window.mainloop()
