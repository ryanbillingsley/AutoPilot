"""Screen Record"""
import time
import cv2
import numpy as np
from directkeys import PressKey, ReleaseKey, W, S, A, D
from PIL import ImageGrab

def process_image(original_img):
    """Detects edges of image"""
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200,  threshold2 = 300)
    return processed_img

for i in list(range(4))[::-1]:
    print(i + 1)
    time.sleep(1)

last_time = time.time()
while True:
    # 800x600 windowed mode
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    new_screen = process_image(screen)

    print('up')
    PressKey(W)
    time.sleep(3)
    print('down')
    PressKey(D)

    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
