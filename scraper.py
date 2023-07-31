import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL for the list of brightest stars and other record stars
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Send an HTTP GET request to fetch the HTML content of the page
response = requests.get(START_URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with class="wikitable sortable"
table = soup.find("table", class_="wikitable sortable")

# Initialize the list to store scraped data
scraped_data = []

# Define scrape() method to scrape all column data
def scrape():
    for row in table.find_all("tr")[1:]:
        columns = row.find_all("td")

        # Extracting data from columns
        v_mag = columns[0].text.strip()
        proper_name = columns[1].text.strip()
        bayer_designation = columns[2].text.strip()
        distance_ly = columns[3].text.strip()
        spectral_class = columns[4].text.strip()
        mass_m = columns[5].text.strip()
        radius_r = columns[6].text.strip()
        luminosity_l = columns[7].text.strip()

        # Append the data to the list scraped_data
        scraped_data.append([v_mag, proper_name, bayer_designation, distance_ly, spectral_class, mass_m, radius_r, luminosity_l])

# Call the scrape() method to fetch the data
scrape()

# Create a DataFrame from the scraped data
headers = ["V Mag. (mV)", "Proper name", "Bayer designation", "Distance (ly)", "Spectral class", "Mass (M☉)", "Radius (R☉)", "Luminosity (L☉)"]
stars_df = pd.DataFrame(scraped_data, columns=headers)

# Export DataFrame to CSV
stars_df.to_csv("stars_data.csv", index=False)
