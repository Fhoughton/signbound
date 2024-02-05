# Signbound
Signbound is a python script and library that can be used to programmatically convert images to signs in the video game [Starbound](https://store.steampowered.com/app/211820/Starbound/).

The game features a pixel art editor to create signs, this tool simply automates the process of converting traditional images and pixel art into signs.

![](https://i.imgur.com/sMKih4M.png)

It has:
- A library, starbound_lib.py, which can be used to command the editor
- A command line utility, main.py that can convert images into signs, including gifs which become animated signs

## Dependencies:
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [keyboard](https://pypi.org/project/keyboard/)
- [Pillow](https://pypi.org/project/pillow/)
