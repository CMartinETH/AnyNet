"""
This module is intended to be used to test the inference of the network and store the output for a stereo image pair.
"""
import os
import numpy as np
from PIL import Image
import torchvision.transforms as tf


def store_image(location, image):
    # cpu_img = unsqueeze(0)image.cpu()
    cpu_img1 = image.cuda().detach().cpu()
    cpu_img2 = image.cuda().detach().cpu().numpy()

    name = filename_check("{}{}".format(location, "result_disp_"), ".png")
    # img = tf.ToPILImage()(cpu_img1)
    # img.save(name)  # write to png

    img_1 = Image.fromarray(np.uint8(cpu_img2))
    img_1.save(name)


def filename_check(fullname, filetype):
    i = 0
    while os.path.exists("{}{}{}".format(fullname, i, filetype)):
        i += 1
    new_name = "{}{}{}".format(fullname, i, filetype)
    return new_name
