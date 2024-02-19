import os, time
from math import sin, cos
def c():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin():
    progress_bar()
    a = 0
    b = 0
    progress = 0

    height = 24
    width = 80
    #c = "cls" if os.name == "nt" else "c"

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

def progress_bar():
    c()
    bar_width = 50
    animation = ["\\", "|", "/", "-"]
    an = ["+", "×"]
    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * bar_width)
        bar = '|' * filled_width + '·' * (bar_width - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))
        print(f'LOADING: {an[ai]} [{bar}] {an[ai]} {percent}% {animation[animation_index]}', end='\r')
        time.sleep(0.1)
if __name__ == "__main__":
    spin()
