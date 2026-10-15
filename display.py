import sys
sys.path.append('lib')  # Ensure the library path is correct
from waveshare_epd import epd7in5_V2  # Adjust the import based on your specific model
from PIL import Image

import os
import time 
import json
def display_single_image(image_file):
    
    # Initialize and clear the display
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()

    # Load the processed image
    image = Image.open(f'{image_file}')

    # Display the image
    epd.display(epd.getbuffer(image))

    epd.sleep()
    print('display is sleeping...' )


  
def file_generator(base_path, start=951):
    """
    A generator function that yields files starting from a base path and incrementing
    a numerical suffix until a file does not exist.

    :param base_path: The base path of the files, excluding the numerical suffix.
    :param start: The starting index for the numerical suffix.
    """
    counter = start
    while True:
        # Construct the filename with an incremented counter
        filename = f"{base_path}/frame_{counter:04d}.bmp"  # Assuming the files are .txt files

        # Check if the file exists
        print(f'checking if file exists {filename}')
        if not os.path.exists(filename):
            
            print('restarting reel... ')
            counter = start
            # counter += 15 # if files are all not there
            
            continue
            # break  # If the file does not exist, exit the loop
        
        yield filename  # Yield the existing filename
        
        counter += 1  # Increment the counter for the next iteration

def load_json_file(file_name):
    data_dict = {'image_num': 0}
    if not os.path.isfile(file_name):
        return data_dict
    with open(file_name, 'r') as file:
        data_dict = json.load(file)
        return data_dict

def save_dict_json_file(file_name, payload_dict):
    with open(file_name, 'w') as file:
        json.dump(payload_dict, file)
        
        
        
def display_images_to_eink(directory):
    
    
    image_payload = load_json_file('image_payload.json' )
    
            
    for entry in file_generator(directory, image_payload['image_num']):
        file_name = entry.split('/')[1]
        file_name = file_name.split('.')[0]
        
        print(f'displaying... steam_boat_willie/{file_name}')
        display_single_image(f'steam_boat_willie/{file_name}')
        
        time.sleep(120)
        
        
        
        
        
        
#display_images_to_eink('steam_boat_willie')
display_single_image('/home/pi/git/eink_display/images/2025-01-01.bmp')
