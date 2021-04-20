from PIL import Image
import glob
import random
import os
import shutil


def get_name(path):
    name_with_ending = path.split('/')[-1]
    return name_with_ending


'''
root_path = '/storage/carla_daten4/'
img_list = sorted(glob.glob(root_path + '*png'))

print(img_list[0:10])
print(get_name(img_list[0]))

#img_list = img_list[0:10]

for img in img_list[::2]:
    im_op = Image.open(img)
    im_op_1 = im_op.resize((256, 256))
    out_name = get_name(img)
    im_op_1.save('/home/schober/stargan-v2/data/a2d2_carla/train/carla/' + out_name)

# a2d2 images

path = '/storage/Audi/camera_lidar_semantic_bboxes/20180807_145028/camera/cam_front_center/20180807145028_camera_frontcenter_000000091.png'
root_path = '/storage/Audi/camera_lidar_semantic_bboxes/'
img_list = glob.glob(root_path + '*/camera/cam_front_center/*.png')






img_name = get_name(path)
print(img_name)
print(len(img_list))

for img in img_list:
    im_op = Image.open(img)
    im_op_1 = im_op.resize((256, 256))
    out_name = get_name(img)
    im_op_1.save('/home/schober/stargan-v2/data/a2d2_carla/train/a2d2/' + out_name)

'''


def get_percentage_list(file_list, number_images):
    out_list  = random.sample(file_list, number_images)
    return out_list


def move_file(input_list, out_dir):
    for file in input_list:
        out_name = get_name(file)
        shutil.move(file, out_dir + out_name)


# move 20% to val folder
a2d2_path = '/home/schober/stargan-v2/data/a2d2_carla/train/a2d2/'
a2d2_file_list = glob.glob(a2d2_path + '*png')
number_a2d2 = int(len(a2d2_file_list) * 0.2)
print(number_a2d2)

carla_path = '/home/schober/stargan-v2/data/a2d2_carla/train/carla/'
carla_file_list = glob.glob(carla_path + '*png')
number_carla = int(len(carla_file_list) * 0.2)
print(number_carla)

val_list_a2d2 = get_percentage_list(a2d2_file_list, number_a2d2)
val_list_carla = get_percentage_list(carla_file_list, number_carla)

out_a2d2 = '/home/schober/stargan-v2/data/a2d2_carla/val/a2d2/'
out_carla = '/home/schober/stargan-v2/data/a2d2_carla/val/carla/'

move_file(val_list_a2d2, out_a2d2)
move_file(val_list_carla, out_carla)

print(val_list_carla[0])
