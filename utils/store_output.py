"""
This module is intended to be used to test the inference of the network and store the output for a stereo image pair.
"""
import os
import PIL
import torchvision.transforms as tf


def store_image(location, image):
    cpu_img = image.cpu()
    name = filename_check("{}{}".format(location, "result_disp_"), ".png")
    img = tf.ToPILImage()(cpu_img)

    img.save(name)  # write to png


def filename_check(fullname, filetype):
    i = 0
    while os.path.exists("{}{}{}".format(fullname, i, filetype)):
        i += 1
    new_name = "{}{}{}".format(fullname, i, filetype)
    return new_name
