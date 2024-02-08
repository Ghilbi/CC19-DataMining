from pinscrape import pinscrape
import requests
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    return BytesIO(response.content)

search_query = "cheese"
output_folder = "output"
zip_filename = "mogged.zip"
max_results = 5
start_index = 15

details = pinscrape.scraper.scrape(search_query, output_folder, {}, max_results, start_index)

if details["isDownloaded"]:
    print("\nDownloading completed !!")
    print(f"\nTotal urls found: {len(details['extracted_urls'])}")
    print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
    print(details)
else:
    print("\nNothing to download !!")
