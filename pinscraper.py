from pinscrape import pinscrape
import requests
from io import BytesIO
import os

def download_image(url):
    response = requests.get(url)
    return BytesIO(response.content)

def save_images(images, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i, image_url in enumerate(images):
        image_data = download_image(image_url)
        with open(os.path.join(output_folder, f"image_{i+1}.jpg"), 'wb') as f:
            f.write(image_data.getbuffer())

search_query = "Cheese"
output_folder = "output"
max_results = 150  # Adjusted to download 150 images
start_index = 150

details = pinscrape.scraper.scrape(search_query, output_folder, {}, max_results, start_index)

if details["isDownloaded"]:
    print("\nDownloading completed !!")
    print(f"\nTotal urls found: {len(details['extracted_urls'])}")
    print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
    
    # Save downloaded images to the output folder
    save_images(details['url_list'], output_folder)
    
    print("\nImages saved to the output folder.")
else:
    print("\nNothing to download !!")