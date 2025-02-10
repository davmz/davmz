import requests
from bs4 import BeautifulSoup

# URL of YouVersion's Verse of the Day page
URL = "https://www.bible.com/verse-of-the-day"

def fetch_verse_of_the_day():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <a> tag where href starts with "/bible/compare/"
    verse_text_tag = soup.find("a", href=lambda x: x and x.startswith("/bible/compare/"))
    verse_text = verse_text_tag.get_text(strip=True) if verse_text_tag else "Unknown Verse"

    # Find the <a> tag where href starts with "/bible/" but NOT "/bible/compare/"
    verse_reference_tag = soup.find("a", href=lambda x: x and x.startswith("/bible/") and "/bible/compare/" not in x)

    # Extract the text inside <p> within this <a> tag
    verse_reference = verse_reference_tag.find("p").get_text(strip=True) if verse_reference_tag else "Unknown Reference"

    return verse_reference, verse_text

def update_readme(verse_reference, verse_text):
    if not verse_reference or not verse_text:
        print("Failed to fetch the verse. Skipping README update.")
        return

    with open("README.md", "r") as file:
        lines = file.readlines()

    with open("README.md", "w") as file:
        in_verse_section = False
        for line in lines:
            if line.strip() == "<!-- START: Verse of the Day -->":
                in_verse_section = True
                file.write(line)
                file.write(f"**📖 {verse_reference}**\n> {verse_text}\n\n")
            elif line.strip() == "<!-- END: Verse of the Day -->":
                in_verse_section = False
            if not in_verse_section:
                file.write(line)

if __name__ == "__main__":
    verse_reference, verse_text = fetch_verse_of_the_day()
    print(f"Verse Reference: {verse_reference}")  # Debugging
    print(f"Verse Text: {verse_text}")  # Debugging
    update_readme(verse_reference, verse_text)