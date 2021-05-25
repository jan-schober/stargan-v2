import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

file_path = "/home/schober/stargan-v2/data/a2d2_carla/ssim_a2d2.json"

def lineplot(path,ssim_threshold = 0.8):

    # Get the Sub Dataframe which contains only the rows including the given SSIM Value
    df = pd.read_json(path,precise_float=True)
    ssim_df = df[df["SSIM"] == ssim_threshold]
    ssim_df.reset_index(inplace=True,drop=True)



    my_ticks = np.arange(min(ssim_df.index),max(ssim_df.index) +1,
                         math.ceil(int(len(ssim_df.index)/15)))
    fig, ax = plt.subplots(figsize = (12,15))
    ax.plot(ssim_df.index,ssim_df["Counter in a Row"])
    plt.xticks(my_ticks,ssim_df.iloc[my_ticks]["Ref Image"],rotation = "vertical")
    xmax = ssim_df["Counter in a Row"].idxmax()
    ymax = ssim_df["Counter in a Row"].max()
    print("Most Images were deleted for Ref: {}".format(ssim_df.iloc[xmax]["Ref Image"]))
    print(ssim_df.iloc[xmax]["Deleted Images"][0],ssim_df.iloc[xmax]["Deleted Images"][-1])

    plt.plot(xmax,ymax,"ro")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_ylabel("Deleted Images")
    ax.set_title("SSIM: {}".format(ssim_threshold))
    ax.legend([path.split("_")[0]])


    plt.annotate("Ref Image: {}".format(ssim_df.iloc[xmax]["Ref Image"]),
                 (xmax,ymax),
                 xytext=(xmax,ymax * 1.05),
                 ha="center")
    plt.show()
    ax.figure.savefig("Max-deletedn_.png")


def hist(path,ssim_threshold):
    # Get the Sub Dataframe which contains only the rows including the given SSIM Value
    df = pd.read_json(path, precise_float=True)
    ssim_df = df[df["SSIM"] == ssim_threshold]

    # Show only Images which Del Counter goes above a threshold
    ssim_df = ssim_df[ssim_df["Counter in a Row"] >= ssim_df["Counter in a Row"].mean() +  ssim_df["Counter in a Row"].std()]
    ssim_df.reset_index(inplace=True, drop=True)

    ax = ssim_df.plot(x = "Ref Image",y = "Counter in a Row",kind = "bar", figsize = (15,15))
    ax.tick_params(axis = 'x', labelsize=6)
    ax.set_ylabel("Deleted Images")
    ax.set_title("SSIM: {}".format(ssim_threshold))
    ax.legend([path.split("_")[0]])

    plt.show()
    ax.figure.savefig("histn_.png")



if __name__ == "__main__":
    lineplot(file_path,ssim_threshold=0.9)
    hist(file_path,ssim_threshold=0.9)
