# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:01:46 2022

@author: gabri
"""

'''' Write a python script that scraps wikipedia page.
Use pandas to arrange the data in csv format.
Remove all web tags like <h1> and </b>''''

from bs4 import BeautifulSoup
import requests
import pandas as pd

Wiki_url = 'https://en.wikipedia.org/wiki/World_energy_supply_and_consumption'

html = requests.get(Wiki_url).text
soup = BeautifulSoup(html, 'html.parser')

table_data1 = soup.find('table')

#all_table_data = soup('table', {'class' : 'table'})
#all_paragraphs = soup.find_all('p')

#Function to remove tags
def remove_tags(soup):
    for data in soup(['style', 'script']):
        data.decompose()
    return ' '.join(soup.stripped_strings)

table_data_untagged = (remove_tags(table_data1))







