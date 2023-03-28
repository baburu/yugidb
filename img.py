import os
import urllib.request

# specify the path of the text file
file_path = 'E:\Desktop\yugidb\cards.txt'

# specify the path for saving the images
save_path = 'E:\Desktop\yugidb\cards'

# if save_path does not exist, create it
if not os.path.exists(save_path):
    os.makedirs(save_path)

# read the urls from file and download the images
with open(file_path, 'r') as file:
    for line in file:
        try:
            # use the image name from the url as the file name
            file_name = line.split('/')[-1].strip()
            
            # download the image and save it to the specified path
            urllib.request.urlretrieve(line, os.path.join(save_path, file_name))
            print(f'{file_name} downloaded successfully.')
            
        except Exception as e:
            print(f'Error downloading {file_name}: {e}')