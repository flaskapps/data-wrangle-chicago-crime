import requests
from pathlib import Path

SRC_URL = 'https://data.cityofchicago.org/api/views/x2n5-8w5q/rows.csv?accessType=DOWNLOAD'
STASH = Path('stash')
DATA_PATH = Path(STASH, 'crime-rows.csv')

def get_data():
    resp = requests.get(SRC_URL)
    return resp.text

def save_data(txt):
    DATA_PATH.write_text(txt)
    return DATA_PATH

def bootstrap():
    STASH.mkdir(exist_ok=True)
    txt = get_data()
    save_data(txt)
    return txt



if __name__ == '__main__':
    print("BOOTSTRAPPING DATA")
    print("Downloading", SRC_URL)
    txt = bootstrap()
    print("Downloaded", len(txt))
