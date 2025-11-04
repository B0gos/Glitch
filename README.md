# Glitch
A small python program that creates a full-screen glitch effect.

How does it work?
1. Waits for a random period of time
2. Takes a Screenshot
3. Distorts and applies effects to recorded screenshot
4. Displays screenshot in a full-screen window
5. Repeats steps 2-4 to animate the glitch effect.
6. Returns to step 1.

I wrote this like 6 years ago during covid, was tested with X11 on a linux system.
May have compatability issue with newer python packages or versions, as well as windows/mac/linux(with wayland) systems.
Potential security risk, as it stores a screencapture in program directory during runtime.

### Usage
1. Create a venv in {project_root}/"venv"
2. Enter the venv with ./venv/bin/activate
3. run pip install -r "requirements.txt"
4. Exit the venv and run start.sh or start.bat depending on your system.
