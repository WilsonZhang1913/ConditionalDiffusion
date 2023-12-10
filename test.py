import os
import os.path
import hashlib
import errno
from torch.utils.model_zoo import tqdm
from PIL import Image
import os


# with open('/home/wilsonzhang/WeatherDiffusion/scratch/ozan/data/allweather/allweather.txt', 'w') as f:
#     for idx in range(861):
#         f.write(f'train/data/{idx}_rain.png')
#         f.write('\n')

# with open('/home/wilsonzhang/WeatherDiffusion/scratch/ozan/data/allweather/allweather_test.txt', 'w') as f:
#     for idx in range():
#         f.write(f'test_a/data/{idx}_rain.png')
#         f.write('\n')



def resize_images(img1_path, img2_path, output_path, spacing=10):
    
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    img1 = img1.resize(img2.size, Image.ANTIALIAS)


    img1.save(output_path)

original_path  = 'scratch/ozan/data/allweather/test_a/data'
output_path    = 'results/images/AllWeather/snow'
combine_path   = 'results/images/AllWeather/original_rain'

for i in range(58):
    orig_img = os.path.join(original_path, f'{i}_rain.png')
    modified_img = os.path.join(output_path, f'{i}_rain_output.png')
    output_img = os.path.join(combine_path, f'{i}_rain.png')
    resize_images(orig_img, modified_img, output_img)