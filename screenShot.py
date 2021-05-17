import pyautogui
import sys
import subprocess
import time

args = sys.argv
dirName = args[1]
pages = int(args[2])

def main():
    path = ".\\books\\{0}".format(dirName)
    res = subprocess.run(["mkdir", path], shell=True)

    for i in range(pages):
        # 635 1346 635
        # 70  70   1079
        screenshot = pyautogui.screenshot(region = (635, 70, 711, 1009))
    
        fileName = "./books/{0}/{1}.png".format(dirName,i)
        screenshot.save(fileName)
        nextPage()
    
def nextPage():
    # 1685 526
    pyautogui.click(x=1685, y=526, button='left')
    time.sleep(1)

if __name__ == "__main__":
    main()