import csv
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

def scrape_url(url):
    """Scrapes the content of the given URL using requests and BeautifulSoup."""
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text(separator='\n', strip=True)
        else:
            return f"Failed to retrieve {url}, status code: {response.status_code}"
    except Exception as e:
        return f"Error retrieving {url}: {e}"

def scrape_from_csv(csv_path, output_path):
    """Scrapes content from a CSV file and writes the scraped content to an output file."""
    with open(csv_path, newline='') as csvfile, open(output_path, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  
                url = row[0]
                content = scrape_url(url)
                outfile.write(content + '\n' + ('=' * 100) + '\n')

csv_path = 'links.csv'
output_path = 'scraped.txt'

scrape_from_csv(csv_path, output_path)
