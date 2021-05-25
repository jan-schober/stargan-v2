from PIL import Image
import glob

def image_grid(imgs, rows, cols):
    print(len(imgs))
    assert len(imgs) == rows *cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size= (cols*w, rows*h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

list_src = sorted(glob.glob('/media/jan/TEST/_Masterarbeit/results/results_star_gan/vergleich/carla_resized/*.jpg'))
list_a2d2 = sorted(glob.glob('/media/jan/TEST/_Masterarbeit/results/results_star_gan/vergleich/a2d2/150*.jpg'))
list_city= sorted(glob.glob('/media/jan/TEST/_Masterarbeit/results/results_star_gan/vergleich/city/150*.jpg'))
list_bdd= sorted(glob.glob('/media/jan/TEST/_Masterarbeit/results/results_star_gan/vergleich/bdd/150*.jpg'))
#list_80k = sorted(glob.glob('/media/jan/TEST/result_star_gan/expr_3/generated/gen_80k/*.jpg'))
#list_100k = sorted(glob.glob('/media/jan/TEST/result_star_gan/expr_3/generated/gen_100k/*.jpg'))
white_img = Image.new('RGB', (256,256), (255, 255, 255))

final_list = []
'''
for ref_id in range(0, 5):
    final_list = []
    final_list.extend([list_src[2]])
    final_list.extend([list_src[1]])
    final_list.extend([list_src[3]])
    final_list.extend([list_src[4]])
    final_list.extend([list_src[0]])
    final_list.extend([list_ref[ref_id]])
    for i in list_20k[ref_id::5]:
        final_list.extend([i])
    final_list.extend([list_ref[ref_id]])
    for i in list_40k[ref_id::5]:
        final_list.extend([i])
    final_list.extend([list_ref[ref_id]])
    for i in list_60k[ref_id::5]:
        final_list.extend([i])
    final_list.extend([list_ref[ref_id]])
    for i in list_80k[ref_id::5]:
        final_list.extend([i])
    final_list.extend([list_ref[ref_id]])
    for i in list_100k[ref_id::5]:
        final_list.extend([i])
'''
for file in list_src:
    final_list.append(file)
for file in list_a2d2:
    final_list.append(file)
for file in list_city:
    final_list.append(file)
for file in list_bdd:
    final_list.append(file)
print(list_src)
print(list_a2d2)
print(final_list)
print(len(final_list))
image, *images = [Image.open(file) for file in final_list]

grid = image_grid([image, *images], rows=4, cols = 6)
    #grid.show()

grid.save('/media/jan/TEST/_Masterarbeit/results/results_star_gan/vergleich/150k_Vergleich_Grid.png')
