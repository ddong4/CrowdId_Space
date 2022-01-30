from PIL import ImageGrab
import win32gui
import sys
import cv2 as cv
import numpy as np


def list_window_names():
    # get list of running apps
    top_list, win_list = [], []

    def enum_cb(hwnd, results):
        win_list.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, top_list)
    return win_list


class WindowCapture:

    def __init__(self, window_name):
        win_list = list_window_names()
        window = [(hwnd, title) for hwnd, title in win_list if window_name in title]
        # grab hwnd for first window with match
        try:
            window = window[0]
        except IndexError:
            sys.exit("No window Found, did you open the program?")

        # set window
        self.hwnd = window[0]

        win32gui.SetForegroundWindow(self.hwnd)
        self.bbox = win32gui.GetWindowRect(self.hwnd)
        self.bbox = (self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3])

    def get_screenshot(self):
        """
        Gets screenshot from window
        :return:
        """
        screenshot = np.array(ImageGrab.grab(self.bbox))

        # convert to np array and then RGB to BGR
        screenshot = np.array(screenshot)
        # screenshot = screenshot.astype(np.uint8)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        return screenshot

