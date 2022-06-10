# Input handling
import pyautogui
import keyboard

# Image handling
from PIL import Image
from PIL import GifImagePlugin

# Internals for managing game interactions
from signbound_lib import *

# Time delay and terminal input
import sys
import time

# Adds a small delay for each action since the game can only handle 1 input per frame
pyautogui.PAUSE = 0.05

pause = False

# Hotkey functions
def toggle_pause(_):
    global pause
    pause = not pause


def request_exit(_):
    global doexit
    doexit = True

# Main program
def main():
    """The main command line loop, used only when the script is directly invoked"""
    if len(sys.argv) != 2:
        print("Call the program in the format: python main.py <file>")
        exit()

    # Establish hotkeys
    keyboard.on_press_key("p", toggle_pause)
    keyboard.on_press_key("q", request_exit)

    delay = 5  # Included to allow the user to switch back to the game before starting the script

    print(f"Waiting {delay} seconds before starting...")

    for i in range(delay):
        time.sleep(1)
        if doexit:
            exit()

    # Base gif handling
    img = Image.open(sys.argv[1])
    width, height = img.size

    if width % 32 != 0 or height % 8 != 0:
        print(
            f"Image was {width}x{height}, which is not a with that's a multiple of 32 or a height that's a multiple of 8")

    horizontal_signs = int(width / 32)
    vertical_signs = int(height / 8)
    total_signs = int(horizontal_signs * vertical_signs)

    print(f"Image needs {total_signs} total signs")

    curr_signs = 0

    for v in range(vertical_signs):
        for h in range(horizontal_signs):
            # Individual frames from the loaded animated GIF file
            for frame in range(0, img.n_frames):
                img.seek(frame)
                im = img.crop((h*32, v*8, 32 + (h*32), 8 + (v*8)))
                draw_image(im)

                # Don't continue making new frames if it's the last frame of the gif
                if frame != img.n_frames - 1:
                    new_layer()

            # End of each sign, print and cleart
            print_sign()
            curr_signs += 1

            if curr_signs == 8:
                pause = True
                while pause:
                    pass
                curr_signs = 0

            clear_sign()

    close_canvas()

# Only run main function if explicitly called, enables library style usage of functions
if __name__ == "__main__":
    main()