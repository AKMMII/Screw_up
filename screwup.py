import rotatescreen   #pip install rotate-screen
import time           # also pip install pypiwin32
screen = rotatescreen.get_primary_display()
screen.rotate_to(0)
for i in range(13):
    time.sleep(0.5)
    screen.rotate_to(i*90 % 360)