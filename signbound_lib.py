import pyautogui
from PIL import Image

doexit = False

def fetch_canvas_coordinate(x, y):
    return (760 + x*12, 490 + y*12)

def goto_and_click(coords):
    pyautogui.moveTo(coords[0], coords[1])
    pyautogui.click()

def open_color_menu():
    color_menu_coords = (1238, 477)
    pyautogui.moveTo(color_menu_coords[0], color_menu_coords[1])
    pyautogui.click()

def close_color_menu():
    exit_button_coords = (1000, 618)
    pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
    pyautogui.click()

def close_canvas():
    exit_button_coords = (1278, 388)
    pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
    pyautogui.click()

def print_sign():
    exit_button_coords = (668, 565)
    pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
    pyautogui.click()

def clear_sign():
    exit_button_coords = (666, 467)
    pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
    pyautogui.click()

def get_color_from_palette(red, green, blue):
    """Returns the most similar color from the ingame palette, in coordinates, for a given rgb colour"""
    im = Image.open('ingame_palette.png')
    rgb_im = im.convert('RGB')
    width, height = im.size

    # find most similar colour coordinate
    closest_x = 0
    closest_y = 0
    closest_dist = 999999999999
    for x in range(width):
        for y in range(height):
            r, g, b = rgb_im.getpixel((x, y))

            dist = abs(red - r) + abs(green - g) + abs(blue - b)

            if dist < closest_dist:
                closest_dist = dist
                closest_x = x
                closest_y = y

    r, g, b = rgb_im.getpixel((closest_x, closest_y))

    return (closest_x, closest_y)

def select_color(r, g, b):
    """Selects the nearest color in the editor"""
    x, y = get_color_from_palette(r, g, b)
    pyautogui.moveTo(684+x, 474+y)
    pyautogui.click()

def new_layer():
    """Creates a new image layer, used for animated signs"""
    button_coords = (1044, 615)
    pyautogui.moveTo(button_coords[0], button_coords[1])
    pyautogui.click()

def draw_image(im):
    """Performs the process of drawing the whole image to a single sign frame"""
    rgb_im = im.convert('RGB')
    width, height = im.size

    last_color = None

    if height > 8 or width > 32:
        print("Draw_image got too large an image")

    for y in range(height):
        for x in range(width):
            if doexit:
                exit()

            # Set the pixel colour based off the image
            r, g, b = rgb_im.getpixel((x, y))

            # If it's not the last color then change the color
            if last_color != (r, g, b):
                open_color_menu()
                select_color(r, g, b)
                close_color_menu()
                last_color = (r, g, b)

            # Place the pixel
            coordinate = fetch_canvas_coordinate(x, y)
            pyautogui.moveTo(coordinate[0], coordinate[1])
            pyautogui.click()  # click the mouse
