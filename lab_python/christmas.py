import sys
import time
import os
import random
import threading

# Import winsound for Windows audio
try:
    import winsound
except ImportError:
    winsound = None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_music():
    """Plays Jingle Bells using winsound (Windows only)"""
    if not winsound:
        return

    # Jingle Bells notes (Frequency, Duration)
    # E=329, F=349, G=392, C=261, D=293
    notes = [
        (329, 200), (329, 200), (329, 400), # E E E
        (329, 200), (329, 200), (329, 400), # E E E
        (329, 200), (392, 200), (261, 200), (293, 200), (329, 800), # E G C D E
        (349, 200), (349, 200), (349, 200), (349, 200), (349, 200), # F F F F F
        (329, 200), (329, 200), (329, 200), (329, 200), # E E E E
        (392, 200), (392, 200), (349, 200), (293, 200), (261, 800)  # G G F D C
    ]
    
    while True:
        for freq, dur in notes:
            winsound.Beep(freq, dur)
            time.sleep(0.05) 
        time.sleep(1)

def print_tree(lights):
    tree = [
        "      *      ",
        "     ***     ",
        "    *****    ",
        "   *******   ",
        "  *********  ",
        " *********** ",
        "*************",
        "     ***     ",
        "     ***     "
    ]

    colors = {
        "*": "\033[31m",  
        "o": "\033[32m",  
        "+": "\033[33m",  
        "@": "\033[34m",  
        "#": "\033[35m",  
        "&": "\033[36m"   
    }

    for line in tree:
        for char in line:
            if char == '*':
                color = random.choice(list(colors.values()))
                print(color + char, end="")
            else:
                print(" ", end="")
        print("\033[0m")  


def main():
    # Start music in a separate thread if on Windows
    if winsound:
        music_thread = threading.Thread(target=play_music, daemon=True)
        music_thread.start()
    
    while True:
        clear_console()
        print_tree(10)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
