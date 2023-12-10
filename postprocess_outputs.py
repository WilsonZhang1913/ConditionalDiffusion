from PIL import Image
import os

def combine_images(img1_path, img2_path, 
                   img3_path, img4_path,
                   img5_path, img6_path,
                   img7_path, img8_path,
                   output_path, spacing=10):
    
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    img1 = img1.resize(img2.size, Image.ANTIALIAS)

    img3 = Image.open(img3_path)
    img4 = Image.open(img4_path)
    img3 = img3.resize(img4.size, Image.ANTIALIAS)
    
    img5 = Image.open(img5_path)
    img6 = Image.open(img6_path)
    img5 = img5.resize(img6.size, Image.ANTIALIAS)

    img7 = Image.open(img7_path)
    img8 = Image.open(img8_path)
    img7 = img7.resize(img8.size, Image.ANTIALIAS)

    # Calculate the size of the combined image
    total_width = img1.width*8 + spacing*7
    max_height = max(img1.height, img2.height)

    new_img = Image.new('RGB', (total_width, max_height))

    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width + spacing, 0))
    new_img.paste(img3, ((img1.width + spacing)*2, 0))
    new_img.paste(img4, ((img1.width + spacing)*3, 0))
    new_img.paste(img5, ((img1.width + spacing)*4, 0))
    new_img.paste(img6, ((img1.width + spacing)*5, 0))
    new_img.paste(img7, ((img1.width + spacing)*6, 0))
    new_img.paste(img8, ((img1.width + spacing)*7, 0))

    new_img.save(output_path)

original_path  = 'scratch/ozan/data/allweather/test_a/data'
output_path    = 'results/images/AllWeather/snow'
combine_path   = 'results/images/AllWeather/combined'

for i in range(54):
    orig_img = os.path.join(original_path, f'{i}_rain.png')
    modified_img = os.path.join(output_path, f'{i}_rain_output.png')
    orig_img1 = os.path.join(original_path, f'{i+1}_rain.png')
    modified_img1 = os.path.join(output_path, f'{i+1}_rain_output.png')
    orig_img2 = os.path.join(original_path, f'{i+2}_rain.png')
    modified_img2 = os.path.join(output_path, f'{i+2}_rain_output.png')
    orig_img3 = os.path.join(original_path, f'{i+3}_rain.png')
    modified_img3 = os.path.join(output_path, f'{i+3}_rain_output.png')

    output_img = os.path.join(combine_path, f'before_after_{i}_rain.png')


    combine_images(orig_img, modified_img, 
                   orig_img1, modified_img1, 
                   orig_img2, modified_img2, 
                   orig_img3, modified_img3, 
                   output_img)
