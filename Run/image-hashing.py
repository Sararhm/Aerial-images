#Avoiding duplicates in downloaded images, images might appear similar or
#even be slight variations of the same subject
#requires a strategy to detect and filter out these duplicates

import requests
import os
from PIL import Image
import imagehash
from io import BytesIO

# Function to fetch images from Unsplash
def fetch_unsplash_images(query, num_images, api_key):
    url = 'https://api.unsplash.com/search/photos'
    headers = {'Authorization': 'Client-ID ' + api_key}
    params = {'query': query, 'per_page': num_images}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return [photo['urls']['regular'] for photo in data['results']]

# Function to save images from URLs to local directory
def save_images(img_urls, save_dir, class_name, hash_set):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for idx, img_url in enumerate(img_urls):
        img_data = requests.get(img_url).content
        image = Image.open(BytesIO(img_data))
        img_hash = imagehash.phash(image)
        
        if img_hash in hash_set:
            continue  # Skip saving this image as it's a duplicate

        hash_set.add(img_hash)
        img_name = f"{class_name}_{idx}.jpg"
        img_path = os.path.join(save_dir, img_name)
        with open(img_path, 'wb') as f:
            image.save(f)

# Parameters
api_key = '54jR8HnBS5jmcNXvGJ-3SPYdvNy7TvT__qD30kj84kY'
num_images_per_class = 15
save_directory = 'unsplash_images'
hash_set = set()  # To store image hashes

# List of classes and corresponding keywords
class_keywords = {
    'helicopter': ['Helicopter', 'military helicopter'],
    'aircraft': ['fighter aircraft', 'attack aircraft', 'light aircraft', 'cargo aircraft'],
    'jet': ['private jet'],
    'airplane': ['Airliner', 'Airplane'],
    'drone': ['unmanned aircraft', 'UAV'],
    'kite': ['flying kite', 'delta kite'],
    'paraglider':['paragliding', 'gliding'],
    'bird': ['flying eagle', 'flying falcon']
}

# Iterate over classes and download images
for class_name, keywords in class_keywords.items():
    for keyword in keywords:
        img_urls = fetch_unsplash_images(keyword, num_images_per_class, api_key)
        save_images(img_urls, os.path.join(save_directory, class_name), class_name, hash_set)
        print(f"Images for {class_name} ({keyword}) downloaded successfully.\n")
