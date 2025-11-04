import time
import os
import random
import tkinter
import pyautogui
import glitch_this
from glitch_this import ImageGlitcher
glitcher = ImageGlitcher()

import PIL
from PIL import Image, ImageTk

# list of possable times that the screen_glitch can happen (in seconds)
timelist = [30, 60, 120, 180, 240, 300]


def screen_glitch():
    # Make the screen glitch randomly
    print("picking a time to do stuff...")
    x = random.choice(timelist)  # pick a time to start
    print("waiting till that time...")
    print("which is {} seconds from now".format(x))

    time.sleep(x)  # wait till that amount of time has passed

    # Take a screen shot and save it as screenshot.png
    print("taking a screenshot...")
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screenshot.png')

    # Use glitch-this to add glitch effects to le screenshot
    print("Adding glitch effects to le screenshot...")
    glitch_img = glitcher.glitch_image('screenshot.png', 5, color_offset=True, gif=False, frames=30)
    # glitch_img[0].save('gscreenshot.gif', format='GIF', append_images=glitch_img[1:], save_all=True, duration=2, loop=2)

    # clean up the old screenshot
    print("cleaning up a little bit...")
    os.remove('screenshot.png')

    # Make le screenshot stay fullscreen for 1 second
    print("Making le edited screenshot fullscreen...")
    showPIL(glitch_img)


def showPIL(glitch_img):
    # make the image "glitch_img" be fullscreen for 1 second
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = glitch_img.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        glitch_img = glitch_img.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(glitch_img)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.after(1000, lambda: root.destroy())
    root.mainloop()


while 1 == 1:
    # Start the loop
    screen_glitch()
