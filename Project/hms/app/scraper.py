import requests
from bs4 import BeautifulSoup
import json

def scrape_diseases(base_url, pages=1):
    """
    Scrape disease names and URLs from Mayo Clinic.
    pages: number of pagination pages to scrape (if applicable)
    """
    all_diseases = []

    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping {url} ...")

        response = requests.get(url)
        if response.status_code != 200:
            print(f" Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Mayo Clinic: diseases links are in 'a' tags with href containing '/diseases-conditions/'
        links = soup.find_all("a", href=True)
        for link in links:
            href = link.get("href")
            if "/diseases-conditions/" in href:
                disease_name = link.get_text(strip=True)
                disease_url = f"https://www.mayoclinic.org{href}"
                all_diseases.append({
                    "name": disease_name,
                    "url": disease_url
                })

    return all_diseases

if __name__ == "__main__":
    base_url = "https://www.mayoclinic.org/diseases-conditions"
    diseases = scrape_diseases(base_url, pages=1)

    with open("diseases.json", "w", encoding="utf-8") as f:
        json.dump(diseases, f, ensure_ascii=False, indent=4)

    print(f"Scraping complete! Saved {len(diseases)} diseases into diseases.json")
