#!/sr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyperclip
import urllib.request as ur
from urllib.parse import urljoin
import bs4

link= 'https://www.videor.co.jp/tvrating/backnumber/2018/index.html'

content= bs4.BeautifulSoup(ur.urlopen(link), 'html.parser')

l=content.find('div').find(id='archives').find_all('a')
for each in l:
    page= urljoin(link, each.get('href'))
    out= each.string+'\t'+page+'\t'
    file= bs4.BeautifulSoup(ur.urlopen(page), 'html.parser')
    # print(file.find('div').find(id="anime"))
    soup= file.find('div').find(id="anime")
    data = []
    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    i=0
    while i<len(data):
        item=data[i]
        if 'プリキュア' in  item[0]:
            print(out,item[0]+'\t'+item[-1], )
            break
        i+=1
    if i== len(data):
        print(out,'<'+str(data[-1][-1]))
