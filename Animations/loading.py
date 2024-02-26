import time, os
BAR_WIDTH = 50
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def progress_bar():
    clear() #clear screen
    #Animation characters
    animation = ["\\", "|", "/", "-",]
    an = ["+", "×"]

    # The Animation loops
    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * BAR_WIDTH)
        bar = '|' * filled_width + '·' * (BAR_WIDTH - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))
        print(f'LOADING: {an[ai]} [{bar}] {an[ai]} {percent}% {animation[animation_index]}', end='\r')
        time.sleep(0.1)
    clear()
    print('Done!')

progress_bar()