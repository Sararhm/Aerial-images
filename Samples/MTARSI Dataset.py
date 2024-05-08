#This version involves downloading the MTARSI Dataset (assuming it's in a zip format), 
#unzipping it, and moving or copying the images into your specified directory structure under appropriate class names.

import os
import zipfile
import shutil

# Function to unzip and organize dataset
def organize_dataset(zip_path, extraction_path, target_directory):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    
    # Assuming dataset structure is known and consistent
    for root, dirs, files in os.walk(extraction_path):
        for file in files:
            if file.endswith('.jpg'):  # Check for image files
                source_path = os.path.join(root, file)
                class_name = root.split('/')[-1]  # Assuming folder name is class name
                target_path = os.path.join(target_directory, class_name)
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                shutil.copy(source_path, target_path)

# Parameters
zip_file_path = 'path_to_mtarasi_dataset.zip'  # Modify this path
extraction_directory = 'mtarsi_extracted'
final_image_directory = 'images'

# Organize dataset
organize_dataset(zip_file_path, extraction_directory, final_image_directory)
print("MTARSI dataset added successfully.")
