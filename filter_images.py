# import the necessary packages
import os
import os.path
import time
from itertools import cycle

import cv2
import imutils
import numpy as np
import pandas as pd
from skimage import measure

img_path = ["/home/schober/stargan-v2/data/a2d2_carla/train/a2d2/"]
# Threshold to test
ssim_threshold = [0.8, 0.9]

# Parameters for Adaptive Thresholding to binarize Images
max_output_value = 255
neighorhood_size = 99
subtract_from_mean = 15


def filter_img(img_path, ssim_del, sub_length=np.nan):
    """The function is used to filter images from one directory, which are similar to reduce the dataset to a more diverse set of images

    input:
            -img_path: the path for the directory the images are in
            ####### SSIM:  Exact same Images -> Error = 1 ; No similarity -> Error = 0 #######
            -ssim_del: threshold for SSIM deciding whether to delete the compared image
            #######
    Output:
            - Counter how many images were deleted
            """

    # Load Images and decide how many Images should be checked
    images = sorted(os.listdir(img_path))

    if sub_length is not np.nan:
        sub_len = sub_length
    else:
        sub_len = len(images)

    print("Starting to check: {}".format(sub_len) + " Images")
    print("====================================================\n")
    img_sub = images[0:sub_len]

    # Set the iterator and the Counter
    licycle = cycle(img_sub)
    inarow_count = 0
    reference = next(licycle)

    # Create Empty Dataframe
    df = pd.DataFrame(columns=["SSIM", "Ref Image", "Counter in a Row", "Deleted Images", "Num Img"])
    del_list = list()

    while True:


        ## Iterate Through the Images, If Error < Threshold we add the Reference I2mage and the deleted images to a dataframe
        nextele = next(licycle)
        if (nextele == img_sub[-1]):
            break
        # Get the Reference Image and Binarize it

        image_grey_ref = cv2.imread(os.path.join(img_path, reference),
                                    cv2.IMREAD_GRAYSCALE)

        resized_height = int(0.625 * image_grey_ref.shape[0])

        image_grey_ref = imutils.resize(image_grey_ref, height=resized_height)

        image_binarized_ref = cv2.adaptiveThreshold(image_grey_ref,
                                                    max_output_value,
                                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                    cv2.THRESH_BINARY,
                                                    neighorhood_size,
                                                    subtract_from_mean)

        # Get the next Image and Binarize it
        image_grey_next = cv2.imread(os.path.join(img_path, nextele),
                                     cv2.IMREAD_GRAYSCALE)
        image_grey_next = imutils.resize(image_grey_next, height=resized_height)

        image_binarized_next = cv2.adaptiveThreshold(image_grey_next,
                                                     max_output_value,
                                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                     cv2.THRESH_BINARY,
                                                     neighorhood_size,
                                                     subtract_from_mean)

        # Calculate the Error to decide whether to delete or not
        err = measure.compare_ssim(image_binarized_ref, image_binarized_next, multichannel=True)

        if (err > ssim_del):
            inarow_count += 1
            del_list.append(nextele)

        if ((err <= ssim_del) or (nextele == img_sub[-1])):
            ## Add Elements of Images to delete
            if inarow_count > 0:
                df = df.append({"SSIM": ssim,
                                'Ref Image': reference, "Counter in a Row": inarow_count,
                                "Deleted Images": del_list, "Num Img": sub_len}, ignore_index=True)
            reference = nextele
            inarow_count = 0
            del_list = list()


    return df


# Check for every Path and every Threshold given
for path in img_path:
    df_result = pd.DataFrame()
    start = time.time()
    for ssim in ssim_threshold:
        # Get the Filename as string
        save_str = path.replace(path.split("/")[-1], "") + path.split("/")[-3] + "_" + path.split("/")[-1]
        print('Starting to Filter ' + path, " SSIM : ", ssim)
        print(path)
        # Actually get the Reference Images and the "Should be deleted Images"
        # df = filter_img(path, ssim_del = ssim,sub_length= 20)
        df = filter_img(path, ssim_del=ssim)
        print(df, "\n")

        # Concate the resulting Dataframes and save as .json file
        df_result = pd.concat([df_result, df], ignore_index=True)
        df_result.to_json(save_str + ".json", double_precision=3)
    end = time.time()
    print(end - start)
    print(save_str)
