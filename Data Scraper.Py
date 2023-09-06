import requests
from bs4 import BeautifulSoup
import csv
import os

url = "https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/earthdata-login"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    data_to_save = []

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        data_to_save.append([href])
    for row in data_to_save:
        print(row)

    desktop_path = os.path.expanduser("~/Desktop")
    csv_file_path = os.path.join(desktop_path, "scraped_data.csv")

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data_to_save:
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_path}")
else:
    print(f"Failed to retrieve data from {url} (Status Code: {response.status_code})")
