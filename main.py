import pyautogui,os,pyttsx3

speak = pyttsx3.speak

speak("Enter file name(with extension): ")
file = input("Enter file name(with extension): ")

img = pyautogui.screenshot()
img.save(file)

speak(f"Screenshot saved as {file}")

speak(f"Opening {file} in photos")
os.startfile(file)