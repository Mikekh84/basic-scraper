import requests
from bs4 import BeautifulSoup
import sys
import io
import re

"""HID is Heath Inspection Data"""
HID_DOMAIN = 'http://info.kingcounty.gov'
HID_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
HID_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'B', }

def get_HID_page(**kwargs):
    url = HID_DOMAIN + HID_PATH
    params = HID_PARAMS.copy()
    for key, val in kwargs.items():
        if key in HID_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content, resp.encoding

def write_file(text, filename):
    with io.open(filename, 'wb') as f:
        f.write(data)

def load_HID_page(filename):
    with io.open(filename, 'rb') as data:
        encoded_data = data.read()
    return encoded_data, 'utf-8'

def parse_source(html, encoding='utf-8'):
    parsed_data = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed_data

def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)

def has_two_tds(el):
    is_tr = el.name == 'tr'
    td_childern = el.find_all('td', recursive=False)
    has_two = len(td_childern) == 2
    return is_tr and has_two

if __name__ == '__main__':
    kwargs = {
    'Inspection_Start': '3/3/2013',
    'Inspection_End': '3/3/2016',
    'Zip_Code': '98125'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        data, encoding = load_HID_page('inspection_page.html')
    else:
        data, encoding = get_HID_page(**kwargs)
    doc = parse_source(data, encoding)
    listings = extract_data_listings(doc)
    for listing in listings:
        metadata_rows = listing.find('tbody').find_all(
            has_two_tds, recursive=False)
        print len(metadata_rows)