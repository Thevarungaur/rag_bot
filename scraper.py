import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

PAGES = [
    "https://www.hansrajcollege.ac.in/",
    "https://www.hansrajcollege.ac.in/about/thecollege",
    "https://www.hansrajcollege.ac.in/academics/departments/science/computer-science/courses",
]

MAX_PAGES_TO_SCRAPE = (int)(os.getenv("MAX_PAGES_TO_SCRAPE", 3))


def scrape_page(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a successful response

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the entire page text
        page_text = soup.get_text(separator="\n").strip()

        return url, page_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return url, None

def save_to_file(url, content):
    # Make sure that the directory exists
    os.makedirs("scraped_pages", exist_ok=True)

    filename = os.path.join("scraped_pages", urlparse(
        url).path.strip("/").replace("/", "_") + ".txt")
    if not filename.endswith(".txt"):
        filename += ".txt"

    if os.path.exists(filename):
        print(f"File {filename} already exists. Skipping.")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(content))

    print(f"Saved {url} to {filename}")


def scrape_website():
    # Scrape the NIET website
    for page in PAGES[:MAX_PAGES_TO_SCRAPE]:
        url, content = scrape_page(page)
        save_to_file(url, content)