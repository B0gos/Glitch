import time
import os
import ctypes
import random
# import threading
import turtle
import tkinter
import pyautogui
import glitch_this
# from threading import Thread
from glitch_this import ImageGlitcher
glitcher = ImageGlitcher()


# List of thing done
# 10/14/2020    got a base screen glitcher working(no gif support)
# 10/14/2020    added a random timer(to make the glitcher glitch randomly)
# 10/14/2020    added debug features such as print() and 1 time run
# 10/14/2020    removed comments because debug features replace them (print())
# 10/15/2020    added a kill switch
# 10/15/2020    added gif support(rebuilt fullscreen app)
# 10/15/2020    re-added comments and orginized code
# 10/16/2020   9:30 AM  adjsusted values to make things more appealing
# 10/16/2020   12:30 AM failed to add waldo.py code (reason below)
# (because turtle can tkinter are not compatable when run at same time)
# 10/16/2020   1:30 PM  fixed varables so now they are now local not global
# 10/16/2020   2:40 PM  create a background changing function
# 10/16/2020   2:40 PM  prepare for shrek final functions

# list of possable things left to do:
# 1   add drawing waldo.py to this script
# 2   add dancing shrek gifs to this(3 windows open each time)
# 3(x)add weaker aftershocks to the glitches to give them more effect
# 4   timer so things get worse as time progresses until a climax
# 5   the climax should be when all shrek has been filled which is after 40 min
# 6   end with a glitched unsecapble screen that says "shrek is love," etc...
# 7   slowly spell shreck on the backround


# list of possable times that the screen_glitch can happen (in seconds)
timelist = [60, 120, 180, 240, 300]
# timelist = [1, 1]  # for debug
background = 1

# decode all backrounds and save them
# do this later


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
    glitch_img = glitcher.glitch_image('screenshot.png', 4, color_offset=True,
                                       gif=True, frames=5)
    glitch_img[0].save('gscreenshot.gif', format='GIF',
                       append_images=glitch_img[1:], save_all=True, duration=1)

    # clean up the old screenshot
    print("cleaning up a little bit...")
    os.remove('screenshot.png')

    # Make le screenshot stay fullscreen for 1 second
    print("Making le edited screenshot fullscreen...")
    fullscreen()

    # clean up gscreenshot.gif
    print("Cleaning up again...")
    os.remove('gscreenshot.gif')

    # run draw program if beyond stage 1
    if background > 1:
        screendraw()

    # run shrek gif program if beyond stage 3
    if background > 3:
        screendraw()
    # And repeat


def fullscreen():
    # make the image "glitch_img" be fullscreen for 1 second
    root = tkinter.Tk()

    frame = 0  # reset frame counter

    # make the tkinter canvas cover the whole screen
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.pack()

    # close canvas if esc is pressed
    root.bind("<Escape>", lambda e: exit())

    # change backround while screen glitches
    backgroundchange()

    # put a image on le canvas 7 times then exit tkinter
    for frame in range(5):
        photo = tkinter.PhotoImage(file="gscreenshot.gif", format="gif -index {}".format(frame))
        canvas.create_image(0, 0, anchor='nw', image=photo)
        time.sleep(0.03)
        frame = frame + 1
        root.update()
        print("{} frames shown".format(frame))
    else:
        root.destroy()

    # Run this fullscreen gif thing code
    root.mainloop()


def screendraw():
    # draw stuff on the screen

    time.sleep(5)  # wait till 5 seconds of time has passed then continue

    count = 0
    repeat = 0
    turtle.color('blue')
    for repeat in range(2):
        for counnt in range(88):
            turtle.forward(100)
            turtle.right(178)
            print("turtle is working on layer")
            print(repeat)
            print(count)
            count += 1
        count = 0
        turtle.forward(100)
    turtle.left(90)
    turtle.width(10)
    turtle.forward(500)


def backgroundchange():
    # change wallpaper to spell shrek

    # prepare varables for usage
    global timelist
    global background
    background = background + 1

    # if backround spells shrek then move to final stage
    if background > 5:
        danger()

    # speed up random time when script progresses to stage 2
    if background > 3:
        print("entering shrek level 2...")
        timelist = [1, 15, 30, 45, 60]

    # Change wallpaper to next wallpaper
    print("changing background...")
    print("shrek stage {}".format(background))
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, "background{}.png".format(background) , 0)


def danger():
    # change screen to show final stage
    print("entering final stage...")

    # decode shrekfinalstage gif
    # do this later

    # repeativly show shrekfinalstage gif on screen till process is killed
    while 1 == 1:
        fullscreen()


while 1 == 1:
    # Start the loop
    screen_glitch()
    # threading.Thread(target=screendraw()).start()  # start turtle draw thread
    # exit()  # for debug
