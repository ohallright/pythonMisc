from Modules import fnImage
import pyautogui

# images to scan the page for
## todo, improve by converting to xpaths
picDownload = r'Images/Download.png'
picDownload_SessionCSV = r'Images/Download_SessionCSV.png'
picDownload_LocalDrive = r'Images/Download_LocalDrive.png'
picDownload_Okay = r'Images/Download_Okay.png'
picDownload_Save = r'Images/Download_Save.png'

# user manually navigates to their reports page in nearpod
# user manually selects class sessions they want to download

loop = int(input('Number of Exports:'))

# auto download
for i in range(0,loop,1):
    fnImage.FindClick(picDownload,20)
    fnImage.FindClick(picDownload_SessionCSV)
    fnImage.FindClick(picDownload_LocalDrive)
    
# todo, below is needed for edge functionality
#    fnImage.FindClick(picDownload_Okay)
#    fnImage.FindClick(picDownload_Save)
    pyautogui.press('esc')