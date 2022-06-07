"""
IMPORTS
"""
import pyautogui
import time
import keyboard
from PIL import Image
from PIL import GifImagePlugin
import sys

pyautogui.PAUSE = 0.05
"""
HELPER/MAIN FUNCTIONS
"""
def q_press(_):
  x, y = pyautogui.position()
  print(x,y)

keyboard.on_press_key("q", q_press)

doexit = False

def p_press(_):
  global doexit
  doexit = True

keyboard.on_press_key("p", p_press)

"""
while True:
  x = input("X:")
  y = input("Y:")

  pyautogui.moveTo(int(x),int(y))
"""

def fetch_canvas_coordinate(x, y):
  return (760 + x*12, 490 + y*12)

def open_color_menu():
  color_menu_coords = (1238, 477)
  pyautogui.moveTo(color_menu_coords[0], color_menu_coords[1])
  pyautogui.click()  # click the mouse

def close_color_menu():
  exit_button_coords = (1000, 618)
  pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
  pyautogui.click()  # click the mouse

def close_canvas():
  exit_button_coords = (1278, 388)
  pyautogui.moveTo(exit_button_coords[0], exit_button_coords[1])
  pyautogui.click()  # click the mouse

def get_color_from_palette(red, green, blue):
  im = Image.open('ingame_palette.png')
  rgb_im = im.convert('RGB')
  width, height = im.size

  # print(width, height)

  # find most similar coordinate
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
  
  #print(r,g,b)
  
  return (closest_x, closest_y)

def select_color(r, g, b):
  x, y = get_color_from_palette(r, g, b)

  pyautogui.moveTo(684+x, 474+y)
  pyautogui.click()  # click the mouse

def new_layer():
  button_coords = (1044, 615)
  pyautogui.moveTo(button_coords[0], button_coords[1])
  pyautogui.click()  # click the mouse

def draw_image(im):
  rgb_im = im.convert('RGB')
  width, height = im.size

  last_color = None

  for y in range(8): 
    for x in range(32):
      if doexit:
        exit()

      # Set the pixel colour based off the image
      r, g, b = rgb_im.getpixel((x, y))

      # If it's not the last color then change the color
      if last_color != (r,g,b):
        open_color_menu()
        select_color(r, g, b)
        close_color_menu()
        last_color = (r,g,b) 
      
      # Place the pixel
      coordinate = fetch_canvas_coordinate(x,y)
      pyautogui.moveTo(coordinate[0], coordinate[1])
      pyautogui.click()  # click the mouse


"""
MAIN PROGRAM
"""
if len(sys.argv) != 2:
  print("Call the program in the format: python main.py <file>")
  exit()

delay = 8

print(f"Waiting {delay} seconds before starting...")

for i in range(delay):
  time.sleep(1)
  if doexit:
    exit()

# Base gif handling
imageObject = Image.open(sys.argv[1])

# Display individual frames from the loaded animated GIF file
for frame in range(0,imageObject.n_frames): 
  imageObject.seek(frame)
  im = imageObject
  draw_image(im) 
  new_layer()

close_canvas()

"""
while True:
  pass
"""
