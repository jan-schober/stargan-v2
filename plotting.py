import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_sub_df import get_sub_df


file_path = "/home/schober/stargan-v2/data/a2d2_carla/train_.json"

# Plotting all Thresholds with their overall amount of deleted images
def boxplot(path):
    """
    Create a Barplot to illustrate the amount of images which will be deleted using the SSIM Threshold

    Input:
    - dataframe_path: Path where the Dataframe (created by filter_images.py) is saved
    """
    df = get_sub_df(path)

    # Set the Barplot
    ax = df.plot.bar(legend = False)
    ax.set_ylim(0,105)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("SSIM Value")
    ax.set_ylabel("% of overall Images Deleted")
    ax.legend([path.split("_")[0]])
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + 0.2, p.get_height() + 1.15))
    head, _, _ = file_path.split("/")[-1].partition("_")
    save_path = head + "_B_arplot.png"
    print(save_path)
    ax.figure.savefig(save_path)

if __name__ == "__main__":
    boxplot(path=file_path)
