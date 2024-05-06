import requests
from bs4 import BeautifulSoup
import os

# Function to scrape images from a webpage
def scrape_images(url, save_dir):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all image tags
    img_tags = soup.find_all('img')
    # Iterate over image tags and download images
    for img_tag in img_tags:
        img_url = img_tag['src']
        img_name = os.path.basename(img_url)
        img_path = os.path.join(save_dir, img_name)
        # Download the image
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded: {img_name}")

# Example usage
url = 'https://example.com'
save_directory = 'images'
scrape_images(url, save_directory)
