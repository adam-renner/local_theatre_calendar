import requests
from bs4 import BeautifulSoup
import re

# URL of the McLean Community Players' homepage
url = "https://mcleanplayers.org"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Define a regular expression to match date and time formats
date_pattern = r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w* \d{1,2}"  # Matches dates like "November 26, 2024"
time_pattern = r"\b\d{1,2}:\d{2}(?:\s*[AaPp][Mm]|[AaPp][Mm])\b" # Matches times like "7:30 PM"

# Locate all <p> tags and filter for performance-related content
performance_section = soup.find_all('p')  # Look at all paragraphs


print("Performance Dates and Times:")
for paragraph in performance_section:
    # Replace <br> tags with a placeholder or newline
    for br in paragraph.find_all('br'):
        br.replace_with('\n')
    text = paragraph.get_text(separator="\n", strip=True)
    # Check if the paragraph contains keywords and extract dates and times
    if "performance" in text.lower() or "date" in text.lower():
        dates = re.findall(date_pattern, text)
        times = re.findall(time_pattern, text)
        if dates or times:
            print(f"Section: {text}")
            for date in dates:
                print(f"  Date: {date}")
            for time in times:
                print(f"  Time: {time}")
