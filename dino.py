import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time

color = None



def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    # Cactus
    for i in range(250, 480):
        for j in range(400, 480):
            if data[i, j] < 150:
                hit("up")
                return
    # Bird
    for i in range(250, 420):
        for j in range(350, 400):
            if data[i, j] < 150:
                hit("down")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
'''
        # Draw the rectangle for cactus
        for i in range(250, 300):
            for j in range(400, 480):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(350, 400):
                data[i, j] = 171

        image.show()
        break
'''
