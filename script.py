import pyautogui
import time

# Prompt for the Techline Connect User Name
username = pyautogui.prompt("TLC User Name")

# If nothing is put in to the username prompt
while not username:
    # keep prompting until a username is obtained
    username = pyautogui.prompt("TLC User Name must be provided")

#Prompt for Techline Connect Password
password = pyautogui.password("TLC Password")

#If nothing is put in to the password prompt
while not password:
    #keep prompting until a password is obtained
    password = pyautogui.password("A TLC password must be provided")


# find the browser window with the proper title for the "VSP Logon Form"
browserLogon = pyautogui.getWindowsWithTitle("VSP Logon Form")[0]

#The browser window has to be minimized first when it is opened
browserLogon.minimize()
'''
after minimizing the window, maximizing it will
bring it to the foreground before typing is done
'''
browserLogon.maximize()

#use sleep later to allow the other windows to load
# time.sleep(1)

# globalUserInputLocation = pyautogui.locateOnScreen("globaluserinput.png")

print(browserLogon)

# pyautogui.moveTo(globalUserInputLocation.left + 10, globalUserInputLocation.top + 30)

'''
The typewrite function will allow the inputs to be provided.
using the "\t" character will create a tab input the will focus
from the first input (username) to the next input (password).
After the password is input, the "\n" will be the enter button.

Second argument is interval (in seconds) for each character typed.
'''
pyautogui.typewrite(username + "\t" + password + "\n")

browserLogon.minimize()



