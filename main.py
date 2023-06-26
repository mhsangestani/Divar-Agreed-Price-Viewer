import requests
from bs4 import BeautifulSoup

# Send HTTP GET Request to the divar.ir website and retrieve its HTML content
r = requests.get('https://divar.ir/s/tehran')

# Parse the HTML content using BeautifulSoup library
soup = BeautifulSoup(r.text, 'html.parser')

# Find all elements in the HTML with the class "kt-post-card__body"
vall = soup.find_all(attrs={'kt-post-card__body'})

# Loop through all the found elements
for i in vall:
    # Convert the element to a string representation
    s = str(i.text)
    
    # If the string contains the word "توافقی", which means negotiable in Farsi
    if 'توافقی' in s:
        # Print the string
        print(s)
