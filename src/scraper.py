import requests
from bs4 import BeautifulSoup
import sys
import io

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

# def write_to_HID_page(filename, **kwargs):
#     text, encoding = get_inspection_page(**kwargs)
#     write_file(text, filename)

def load_HID_page(filename):
    with io.open(filename, 'rb') as data:
        encoded_data = data.read()
    return encoded_data, 'utf-8'

def parse_source(html, encoding='utf-8'):
    parsed_data = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed_data




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
    print doc.prettify(encoding=encoding)