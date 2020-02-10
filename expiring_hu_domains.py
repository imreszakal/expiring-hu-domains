# https://github.com/imreszakal/expiring-hu-domains
 
import requests
from bs4 import BeautifulSoup
import sys
import time

timestamp = time.strftime('%Y_%m_%d__%H_%M_%S')

def url(page_index):
    return 'https://www.domainabc.hu/felszabadulo-domainek/?rendezes=4&p=' + str(page_index)

def get_items(page_index):
    print("   %s" % page_index, end="\r")
    page = requests.get(url(page_index))
    items = BeautifulSoup(page.content, 'html.parser').find_all('td')
    items_length = len(items)
    result = [items[i].text + ", " + items[i+1].text for i in range(1, items_length, 3)]
    return result, items_length < 61 

expiring = []
fewer = False
p = 0
while not fewer:
    result, fewer = get_items(p)
    expiring.extend(result)
    p += 1

expiring = sorted(expiring, key=len)

filename = 'expiring_hu_domains___' + timestamp + ".txt"

with open(filename, "a") as file:
    for e in expiring:
        file.write("%s\n" % e)
