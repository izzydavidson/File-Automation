import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def get_url_paths(url, ext=''):
    response = requests.get(url)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent


def main():
    url = 'url'
    ext = '.fastq'
    result = get_url_paths(url, ext) # type: ignore

    for file in result:
        f_name = file[-19, -13]
        r = requests.get(file)
        with open(f'C:/Users/izzydavidson/Desktop/WebScrape', 'wb') as f:
            f.write(r.content)

