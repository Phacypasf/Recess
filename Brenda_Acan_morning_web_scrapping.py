#import libraries
from bs4 import BeautifulSoup
import requests


url ='https://xeno-canto.org'
response= requests.get(url)
# Get the tittle of the website
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('title')
print (title)



#Assignment

import requests

def extract_bird_songs():
    base_url = 'https://xeno-canto.org/api/2/recording'
    page = 1  # Start with page 1
    all_songs = []

    while True:
        url = f'{base_url}?page={page}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            songs = data['recordings']

            if not songs:
                # If the page has no songs, break the loop
                break
            
            all_songs.extend(songs)
            page += 1
        else:
            print(f'Failed to fetch data from page {page}')
            break

    return all_songs

if __name__ == "__main__":
    bird_songs = extract_bird_songs()

    if bird_songs:
        # Now you have a list of all bird songs in 'bird_songs'
        # You can further process or save this data as needed.
        print(f'Total bird songs extracted: {len(bird_songs)}')
    else:
        print('Failed to extract bird songs.')






