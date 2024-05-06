#It's not feasible to gather images from different websites without specifying the URLs of those websites in some way. 
#Web scraping typically involves targeting specific websites or web pages to extract data, including images.
#However, you can automate the process of gathering images from a list of predefined websites or by searching for specific keywords across multiple websites.

import requests
from bs4 import BeautifulSoup
import os

# Function to search and scrape images from Google Images
def scrape_google_images(query, num_images, save_dir):
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', limit=num_images)
    for idx, img_tag in enumerate(img_tags):
        img_url = img_tag['src']
        img_name = f"{query}_{idx}.jpg"
        img_path = os.path.join(save_dir, img_name)
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded: {img_name}")

# Example usage
query = 'cat'
num_images = 10
save_directory = 'images'
scrape_google_images(query, num_images, save_directory)
