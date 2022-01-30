import cv2 as cv
import numpy as np


class Detect:
    # properties
    img = None
    img_width = 0
    img_height = 0
    method = None

    def __init__(self, path='dot.jpg', method=cv.TM_CCOEFF_NORMED):
        self.img = cv.imread(path, cv.IMREAD_UNCHANGED)

        # Save dimensions of ball
        self.img_width = self.img.shape[1]
        self.img_height = self.img.shape[0]

        # other methods include TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find_dot(self, img, threshold=0.8, debug_mode=None):
        """
        Returns top_left location of dot if found on parsed image
        :param img:
        :param threshold:
        :param debug_mode:
        :return:
        """

        # match template of dot
        result = cv.matchTemplate(img, self.img, self.method)

        # get location of best match
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        print('Best match top left position: %s' % str(max_loc))
        print('Best match confidence: %s' % max_val)

        top_left = []

        loc = np.where( result >= (max_val-0.05))

        for top_left in zip(*loc[::-1]):
            print('Found dot.')

            # get dimensions of rect
            bottom_right = (top_left[0] + self.img_width, top_left[1] + self.img_height)
            # draw rectangle around the pinball
            cv.rectangle(img, top_left, bottom_right,
                         color=(0, 255, 0), thickness=1, lineType=cv.LINE_4)
            # cv.imwrite('result.jpg', img)

        else:
            print('Dot not found.')

        if debug_mode:
            cv.imshow('Match', img)

        return top_left
