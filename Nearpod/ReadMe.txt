Nearpod_1414

User setup

use with chrome as browser (only tested on chrome)

will need to pip install
    -pandas
    -pyautogui
    -pillow
    -openpyxl

Notes:
    -the first script takes the number of exports then you click class by class in nearpod
    -the second script takes the first activity (col 7, G)
        -if the value is blank or a "-" then that's a 0, else 1

Errors:
    -you may need to screenshot the 3 buttons to click (in images), they're unstable on my wife's pc but not on mine
    -nearpod allows students to enter in their own name, so some data cleaning may be needed especially if multiple students go by the exact same name
        -it would be helpful if students enter the first letter of their last name etc to help with data (this will also help with class management)
