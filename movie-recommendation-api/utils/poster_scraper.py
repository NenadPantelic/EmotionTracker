import urllib.request
import socket
from bs4 import BeautifulSoup


def scrape_imdb_poster(movie_url):
    try:
        with urllib.request.urlopen(movie_url, timeout=3) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            image_url = soup.find('div', class_='poster').a.img['src']
            extension = image_url[-3:]
            image_url = ''.join(image_url.partition('_')[0]) + extension
            print("Poster URL fetched successfully.")
            return image_url
    except AttributeError as e:
        print(f"Poster URL was not fetched - poster for the imdb movie with the url = {movie_url} cannot be found.")
        return None
    except urllib.error.HTTPError as e:
        print("Poster URL was not fetched - an HTTP error occured during the poster fetching.")
        return None
    except urllib.error.URLError as e:
        print("Poster URL was not fetched - an URL error occured during the poster fetching.")
        return None
    except socket.timeout as e:
        print("Poster URL was not fetched - connection timeout.")
        return None
