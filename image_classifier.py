import cv2
import numpy as np
import os
import shutil

images_dir = './flood_dataset/Dataset/images' 
masks_dir = './flood_dataset/Dataset/labels'   
output_dir = './Sorted_Flood_Dataset'

    

PASSABLE_THRESHOLD = 30.0 # Anything above 30% flood coverage is impassable

# 3. Create the target directories
categories = ['clear', 'passable', 'impassable']
for category in categories:
    os.makedirs(os.path.join(output_dir, category), exist_ok=True)

# 4. Loop through the original images
processed_count = 0
for image_name in os.listdir(images_dir):
    if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue
        
    image_path = os.path.join(images_dir, image_name)
    
   
    # If the masks are PNGs but images are JPGs, adjust the extension:
    mask_name = image_name.replace('image_', 'label_').replace('.jpg', '.png')
    mask_path = os.path.join(masks_dir, mask_name)
    
    if not os.path.exists(mask_path):
        print(f"Skipping {image_name}: No matching mask found.")
        continue

    # 5. Read the mask in grayscale mode
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if mask is None:
        continue
    
    height = mask.shape[0]
    roi_start = int(height * 0.4) 
    roi_mask = mask[roi_start:, :]
        
    # 6. Calculate the percentage of water
    water_pixels = np.sum(mask == 1)
    total_pixels = mask.shape[0] * mask.shape[1]
    water_percentage = (water_pixels / total_pixels) * 100

    # 7. Classify based on the calculated percentage
    if water_percentage == 0:
        target_folder = 'clear'
    elif 0 < water_percentage <= PASSABLE_THRESHOLD:
        target_folder = 'passable'
    else:
        target_folder = 'impassable'

    # 8. Copy the ORIGINAL image to the sorted folder
    destination_path = os.path.join(output_dir, target_folder, image_name)
    shutil.copy(image_path, destination_path)
    processed_count += 1

print(f"Successfully automated the classification of {processed_count} images based on mask data.")