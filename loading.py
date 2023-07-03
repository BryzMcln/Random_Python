import time, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def progress_bar():
    clear()
    bar_width = 50
    animation = ["\\", "|", "/", "-",]
    an = ["+", "×"]
    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * bar_width)
        bar = '|' * filled_width + '·' * (bar_width - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))
        print(f'LOADING: {an[ai]} [{bar}] {an[ai]} {percent}% {animation[animation_index]}', end='\r')
        time.sleep(0.1)