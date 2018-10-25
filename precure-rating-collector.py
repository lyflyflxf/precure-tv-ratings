#!/sr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl
# dir="E:\My Documents\新东方\托福\备课资料\直通车\独立写作高频短语\综合写作 首考必背词汇 汇总.xlsx"
# wb = openpyxl.load_workbook(dir)

# l=wb.get_sheet_names()
# n= [4, 10, 13, 15, 16, 17, 18, 21, 22, 23, 26, 29, 34]
# for i in l:
#     if i[3]==' ':
#         n.append(int(i[4:]))
#     else:
#         n.append(int(i[3:]))
# n.sort()
# print(n,)
# day_s='星期一\t星期二\t星期三\t星期四\t星期五'
# i=0
# k=3
# while i<12//k:
#     l= n[i * k:i * k + 2]
#     print(day_s)
#     for each in l:
#         print('背诵',each,'\t复习',each,'\t',end='')
#     print('背诵',n[i*k+2])
    # print(str(l[0])+'和'+str(l[1]))
    # i+=1

import pandas as pd
import numpy as np
from datetime import *
import os
import pyperclip
import urllib.request as ur
from urllib.parse import urljoin
import bs4

link= 'https://www.videor.co.jp/tvrating/backnumber/2018/index.html'

content= bs4.BeautifulSoup(ur.urlopen(link), 'html.parser')

l=content.find('div').find(id='archives').find_all('a')
# print(l)
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


# print(urljoin(link, l[0].get('href')))
# pyperclip.copy(bs4.BeautifulSoup(file,'html.parser').prettify())
