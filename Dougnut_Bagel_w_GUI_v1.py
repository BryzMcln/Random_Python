import tkinter as tk
import os
import time
from math import sin, cos

#Clear
def c():
    os.system('cls' if os.name == 'nt' else 'clear')

#Doughnut Bagel Spin
def spin():
    a = 0
    b = 0

    height = 24
    width = 80

    # Create a new Tkinter window for the donut animation
    root = tk.Tk()
    root.title("Donut Animation")
    canvas = tk.Canvas(root, width=width*10, height=height*10)
    canvas.pack()

    while True:
        z = [0 for _ in range(4*height*width)]
        screen = [' ' for _ in range(height*width)]

        j = 0
        while j < 6.28:
            j += 0.07
            i = 0
            while i < 6.28:
                i += 0.02

                sinA = sin(a)
                cosA = cos(a)
                cosB = cos(b)
                sinB = sin(b)

                sini = sin(i)
                cosi = cos(i)
                cosj = cos(j)
                sinj = sin(j)

                cosj2 = cosj + 2
                mess = 1/(sini*cosj2*sinA + sinj*cosA + 5)
                t = sini*cosj2*cosA - sinj*sinA

                x = int(40 + 30*mess*(cosi*cosj2*cosB - t*sinB))
                y = int(11 + 15*mess*(cosi*cosj2*sinB + t*cosB))
                o = int(x + width*y)
                N = int(8*((sinj*sinA - sini*cosj*cosA)*cosB - sini*cosj*sinA - sinj*cosA - cosi*cosj*sinB))

                if 0 < y < height and 0 < x < width and z[o] < mess:
                    z[o] = mess
                    screen[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

        c()
        for index, char in enumerate(screen):
            if index % width == 0:
                print()
            else:
                print(char, end='')
        a += 0.04
        b += 0.02

        root.update_idletasks()
        root.update()

def progress_bar():
    c()
    bar_width = 50
    animation = ["\\", "|", "/", "-"]
    an = ["+", "×"]

    # Create a new Tkinter window for the loading animation
    root = tk.Tk()
    root.title("LOADING PLEASE WAIT...")

    percent_label = tk.Label(root, text="")
    percent_label.pack()

    bar_label = tk.Label(root, text="", width=bar_width)
    bar_label.pack()

    animation_label = tk.Label(root, text="")
    animation_label.pack()

    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * bar_width)
        bar = '|' * filled_width + '·' * (bar_width - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))

        percent_label.config(text=f"LOADING: {an[ai]} {percent}%")
        bar_label.config(text=bar)
        animation_label.config(text=animation[animation_index])

        time.sleep(0.1)
        root.update_idletasks()
        root.update()

    root.destroy()
    spin()

def start_animation():
    root.destroy()
    progress_bar()

# Create the main Tkinter window
root = tk.Tk()
root.title("WELCOME")
start_button = tk.Button(root, text="LETS GO!!!", command=start_animation)
start_button.pack()

root.mainloop()
