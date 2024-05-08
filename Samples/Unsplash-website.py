import requests
import os

# Function to fetch images from Unsplash
def fetch_unsplash_images(query, num_images, api_key):
    url = 'https://api.unsplash.com/search/photos'
    headers = {'Authorization': 'Client-ID ' + api_key}
    params = {'query': query, 'per_page': num_images}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return [photo['urls']['regular'] for photo in data['results']]

# Function to save images from URLs to local directory
def save_images(img_urls, save_dir, class_name):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for idx, img_url in enumerate(img_urls):
        img_name = f"{class_name}_{idx}.jpg"
        img_path = os.path.join(save_dir, img_name)
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as f:
            f.write(img_data)

# Parameters
api_key = 'YOUR_UNSPLASH_API_KEY'  # Replace with your actual API key
num_images_per_class = 15
save_directory = 'unsplash_images'
query = 'airplanes'  # Example query

# Fetch and save images
img_urls = fetch_unsplash_images(query, num_images_per_class, api_key)
save_images(img_urls, save_directory, query)
print("Images downloaded successfully.")
