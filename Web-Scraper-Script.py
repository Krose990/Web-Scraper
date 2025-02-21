import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape (Example: BBC News)
url = "https://www.bbc.com/news"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract headlines
    headlines = []
    for item in soup.find_all("h3"):
        headlines.append(item.get_text())

    # Save headlines to a CSV file
    df = pd.DataFrame(headlines, columns=["Headlines"])
    df.to_csv("news_headlines.csv", index=False)
    
    print("Scraped headlines saved to news_headlines.csv")
else:
    print("Failed to fetch the page.")

