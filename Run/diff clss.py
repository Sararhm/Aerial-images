#Takes different keywords representing different classes and searches for images related to each class, extracting their URLs

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os

# Function to search for images on Google Images and extract image URLs
def search_images(query, num_images):
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', limit=num_images)
    img_urls = [img['src'] for img in img_tags]
    for i, url in enumerate(img_urls):
        if not url.startswith('http'):
            img_urls[i] = 'https://' + url

    return img_urls

# Function to save images from URLs to local directory
def save_images(img_urls, save_dir, query):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for idx, img_url in enumerate(img_urls):
        if not urlparse(img_url).hostname:
            print(f"Skipping invalid URL: {img_url}")
            continue

        img_name = f"{query}_{idx}.jpg"
        img_path = os.path.join(save_dir, img_name)
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded: {img_name}")

# List of classes and corresponding keywords
class_keywords = {
    'helicopter': ['Helicopter', 'military helicopter'],
    'aircraft': ['fighter aircraft', 'attack aircraft', 'light aircraft', 'cargo aircraft'],
    'jet': ['Business jet'],
    'airplane': ['Airliner', 'Airplane'],
    'drone': ['unmanned aircraft', 'UAV/UAM', 'UAV/UAS', 'UAV', 'Unmanned Aerial Vehicle'],
    'kite': ['flying kite', 'delta kite'],
    'bird': ['eagle', 'falcon', 'canadian goose', 'crow']
    # Add more classes and keywords as needed
}

# Parameters
num_images_per_class = 10
save_directory = 'images'

# Iterate over classes and search for images
for class_name, keywords in class_keywords.items():
    print(f"Searching for images of {class_name}...")
    img_urls = search_images(keywords, num_images_per_class)
    print(f"Found {len(img_urls)} images for {class_name}. Downloading...")
    save_images(img_urls, save_directory, class_name)
    print(f"Images of {class_name} downloaded successfully.\n")
