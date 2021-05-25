import pandas as pd


def get_sub_df(path):
    """
    Get Sub Dataframe and List the Amount of Images
    which will be deleted with the Corresponding SSIM Threshold


    Input:
    - The Path the Json File is saved in

    Output:
    - Return A Dataframe with the SSIM Threshold and the amount
        of images which would be deleted in percent
    """

    df = pd.read_json(path,precise_float=True)
    total = df.groupby(["SSIM"]).sum().drop(["Num Img"],axis = 1)*100/(df["Num Img"][0])
    print(df)

    total = total.round({"SSIM":2}).rename(columns = {'Counter in a Row':"Percentage of deleted Images"})
    total = total.round({"Percentage of deleted Images":3})
    print(total)

    return total


if __name__ == "__main__":
    get_sub_df()