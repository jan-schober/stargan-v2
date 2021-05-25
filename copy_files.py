from shutil import copyfile
import glob

#root_path_src = '/home/schober/bdd100k/images/100k/val/'
root_path_src = '/storage/Cityscapes/cityscape_dataset/leftImg8bit/val/'
root_path_dst = '/home/schober/stargan-v2/data/city_carla/val/city/'

src_list =glob.glob(root_path_src +'*/*.png' )

i = 0
max_i = len(src_list)

for file in src_list:
    file_name = file.split('/') [-1]

    dst_nama = root_path_dst + file_name
    copyfile(file, dst_nama)
    print(str(i) + ' / ' + str(max_i))
    i+=1
