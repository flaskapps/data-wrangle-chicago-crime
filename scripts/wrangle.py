import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))

from bootstrap import DATA_PATH as RAW_DATA_PATH
import csv
from pathlib import Path

DATA_DIR = Path('static', 'data')
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_PATH = Path(DATA_DIR, 'crimes.csv')


WRANGLED_HEADERS = [
    'category',
    'sub_category',
    'arrest_made',
    'latitude',
    'longitude',
]

def read_raw_data():
    txt = RAW_DATA_PATH.read_text()
    lines = txt.splitlines()
    data = list(csv.DictReader(lines))

    return data

def filter_crimes(records):
    data = []
    for row in records:
        if 'GUN' in row[' SECONDARY DESCRIPTION']:
            k = __fixrow(row)
            data.append(k)
    return data

def __fixrow(row):
    d = {}
    d['sub_category'] = row[' SECONDARY DESCRIPTION']
    d['category'] = row[' PRIMARY DESCRIPTION']
    d['arrest_made'] = row['ARREST']
    d['latitude'] = row['LATITUDE']
    d['longitude'] = row['LONGITUDE']
    return d


def wrangle():
    raw_records = read_raw_data()
    print("Raw data has", len(raw_records), "records")

    filtered_records = filter_crimes(raw_records)
    print("Filtered data has", len(filtered_records), "records")

    # headers is just the list of key names for any given dict
    # in the records
    headers = filtered_records[0].keys()


    with open(DATA_PATH, 'w') as f:
        w = csv.DictWriter(f, fieldnames=WRANGLED_HEADERS)
        w.writeheader()
        w.writerows(filtered_records)









if __name__ == "__main__":
    wrangle()
