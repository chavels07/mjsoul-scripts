# -*- coding: utf-8 -*-
# @File: base.py
# @Time: 2024/1/12 22:43
# @Description:

import requests

BASE_URL = 'https://game.maj-soul.com/1/'

response = requests.get(BASE_URL + 'version.json')
print('current version for MajSoul:', response.text)
