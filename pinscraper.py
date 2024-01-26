from pinscrape import pinscrape
from zipfile import ZipFile
import os
import requests
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    return BytesIO(response.content)

def save_to_zip(images, zip_filename):
    with ZipFile(zip_filename, 'w') as zip_file:
        for image_url in images:
            image_data = download_image(image_url)
            zip_file.writestr(os.path.basename(image_url), image_data.read())

search_query = "jordan barret"
output_folder = "output"
zip_filename = "mogged.zip"
max_results = 5
start_index = 15

details = pinscrape.scraper.scrape(search_query, output_folder, {}, max_results, start_index)

if details["isDownloaded"]:
    print("\nDownloading completed !!")
    print(f"\nTotal urls found: {len(details['extracted_urls'])}")
    print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")

    # Save downloaded images to a zipfile
    save_to_zip(details['url_list'], zip_filename)
    
    print(f"\nImages saved to {zip_filename}")
    print(details)
else:
    print("\nNothing to download !!")