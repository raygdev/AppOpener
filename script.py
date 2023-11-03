import pyautogui
import time

#use sleep later to allow the other windows to load
time.sleep(7)

# Prompt for the Techline Connect User Name
TLCusername = pyautogui.prompt("TLC User Name")

# If nothing is put in to the username prompt
while not TLCusername:
    # keep prompting until a username is obtained
    TLCusername = pyautogui.prompt("TLC User Name must be provided")

#Prompt for Techline Connect Password
TLCpassword = pyautogui.password("TLC Password")

#If nothing is put in to the password prompt
while not TLCpassword:
    #keep prompting until a password is obtained
    TLCpassword = pyautogui.password("A TLC password must be provided")



cdkUsername = pyautogui.prompt("CDK username")

cdkPassword = pyautogui.password("CDK password")

while not cdkUsername:
     cdkUsername = pyautogui.prompt("CDK username")

while not cdkPassword:
     cdkPassword = pyautogui.password("CDK password")


# find the browser window with the proper title for the "VSP Logon Form"
browserLogon = pyautogui.getWindowsWithTitle("VSP Logon Form")[0]
cdkLogon = pyautogui.getWindowsWithTitle("CDK")[0]
powershell = pyautogui.getWindowsWithTitle("PowerShell")[0]
powershell.minimize()
cdkLogon.minimize()

#The browser window has to be minimized first when it is opened
browserLogon.minimize()

cdkLogon.maximize()
time.sleep(5)
pyautogui.typewrite(cdkUsername)
pyautogui.press("tab")
pyautogui.typewrite(cdkPassword)
pyautogui.press("enter")
cdkLogon.minimize()
'''
after minimizing the window, maximizing it will
bring it to the foreground before typing is done
'''
browserLogon.maximize()
time.sleep(2)

'''
The typewrite function will allow the inputs to be provided.
using the "\t" character will create a tab input the will focus
from the first input (username) to the next input (password).
After the password is input, the "\n" will be the enter button.

Second argument is interval (in seconds) for each character typed.
'''
pyautogui.typewrite(TLCusername + "\t" + TLCpassword + "\n")

browserLogon.minimize()
