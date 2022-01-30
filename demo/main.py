import cv2 as cv
import numpy as np
from time import time

import detect
from windowcapture import WindowCapture
from detect import Detect


def main():
    VIDEO_WINDOW_NAME = 'VLC media player'

    win_cap = WindowCapture(VIDEO_WINDOW_NAME)
    dot_detect = Detect()
    loop_time = time()

    while True:

        screenshot = win_cap.get_screenshot()
        # cv.imshow('Computer Vision', screenshot)/z

        # return dot if detected
        point = dot_detect.find_dot(screenshot, debug_mode=True)

        # FPS to console
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        # press 'q' with the output window focused to exit.
        # wait 1ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


if __name__ == "__main__":
    main()