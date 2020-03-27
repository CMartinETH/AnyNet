"""
This module is intended to be used to test the inference of the network and store the output for a stereo image pair.
"""
import os
import numpy as np

import cv2


def store_image(location, image):
    for i in range(image.size()[0]):
        img_cpu = np.asarray(image.cpu())
        img_save = np.clip(img_cpu[i, :, :], 0, 256)
        img_save = (img_save * 256.0).astype(np.uint16)
        name = filename_check("{}{}{}".format(location, "/", "result_disp_"), ".png")
        cv2.imwrite(name, img_save)


def filename_check(fullname, filetype):
    i = 0
    while os.path.exists("{}{}{}".format(fullname, i, filetype)):
        i += 1
    new_name = "{}{}{}".format(fullname, i, filetype)
    return new_name
