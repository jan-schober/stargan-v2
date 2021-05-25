import pandas as pd
import os

ssim_threshold = 0.9
directory_path = "/home/schober/stargan-v2/data/a2d2_carla/train/a2d2"
dataframe_path = "/home/schober/stargan-v2/data/a2d2_carla/train_.json"


def delete_imgs(ssim_threshold,path,dataframe_path):
    """
    Input:
    - SSIM Threshold: The Threshold which shall be used to delete the corresponding Images
    - Path          : The Path where the Images are saved in
    - dataframe_path: Path where the Dataframe (created by filter_images.py) is saved

    Output:
    - None
    """

    # Get the Sub Dataframe which contains only the rows including the given SSIM Value
    df = pd.read_json(dataframe_path)
    ssim_df = df[df["SSIM"] == ssim_threshold]

    # Get The list of Images which will be deleted
    del_list = list(set([a for b in ssim_df["Deleted Images"].tolist() for a in b]))


    print("Starting to Delete: {}".format(len(del_list)) + " Images")
    print("=======================================================\n")
    # Delete the Files in the given Directory
    for f in del_list:
        if os.path.exists(os.path.join(path,f)) is True:
            os.remove(os.path.join(path,f))
            print("deleteting:{}".format(f))

        else:
            print("{} has been deleted already".format(f))


if __name__ == "__main__":
    delete_imgs(ssim_threshold=ssim_threshold,
                path = directory_path,
                dataframe_path= dataframe_path)
