#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'https://cableexpress.co/category/7/%D7%97%D7%93%D7%A9%D7%95%D7%AA-%D7%A2%D7%95%D7%9C%D7%9D-%D7%94%D7%AA%D7%97%D7%91%D7%95%D7%A8%D7%94'
print(BeautifulSoup(requests.get(url).content, 'html.parser').find('div',id='divMainContent').text)

