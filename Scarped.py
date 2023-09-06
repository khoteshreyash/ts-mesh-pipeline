import requests
from bs4 import BeautifulSoup
import csv
import os

# Define the URL you want to scrape
url = "https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/earthdata-login"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scraping data (replace this with your data extraction logic)
    data_to_save = []

    # Example: Extract all links on the page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        data_to_save.append([href])

    # Display the extracted data
    for row in data_to_save:
        print(row)

    # Define the path to your desktop and the CSV file
    desktop_path = os.path.expanduser("~/Desktop")
    csv_file_path = os.path.join(desktop_path, "scraped_data.csv")

    # Write the data to a CSV file on your desktop
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data_to_save:
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_path}")
else:
    print(f"Failed to retrieve data from {url} (Status Code: {response.status_code})")
