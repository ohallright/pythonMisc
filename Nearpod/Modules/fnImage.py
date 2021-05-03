## Author: Ryan L 2021, gitHub ohallright/pythonMisc

import pyautogui
import time

# search page button, then click
def FindClick(picture, seconds=10):      
    seconds = int(seconds)
    
    # print(seconds, 'seconds')
    for i in range(seconds):
        loc = pyautogui.locateOnScreen(picture)
        # print(loc)
        # print(i)
        if (loc != None): break
        time.sleep(.2)
    if (loc != None):
        pyautogui.click(loc)
        output = 'Clicked'
    if (loc == None):
        output = 'NotFound'
    return output
        
# search page button
def FindPic(picture, seconds=10):
    # print(seconds, 'seconds')
    for i in range(seconds):
        loc = pyautogui.locateOnScreen(picture)
        if (loc != None): break
        time.sleep(.2)    
    if (loc != None):
        output = 'Found'
    if (loc == None):
        output = 'NotFound'
    return output    
