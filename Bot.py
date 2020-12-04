# Barry! Breakfast is ready!
# Coded by Emir Tanır
# Python Spambot
# Try this on whatsapp web

import pyautogui,time

fuel = open("fuel.txt","r")

print("Bot will start in 5 seconds.")
time.sleep(5)

for word in fuel:
    pyautogui.typewrite(word)
    pyautogui.press("enter")