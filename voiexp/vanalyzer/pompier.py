# -*- coding: utf-8 -*-
import os
import locale
import sys
import datetime
import re
import requests
from bs4 import BeautifulSoup

def get_html(url):
    cache_file = '/tmp/pompier.html'
    if os.path.isfile(cache_file):
        with open(cache_file, 'r') as f:
            text = f.read()
    else:
        r = requests.get(url)
        text = r.text
        with open(cache_file, 'w') as f:
            f.write(text)
    return text

locale.setlocale(locale.LC_ALL, 'FI_fi')
weekday = datetime.datetime.now().strftime('%A')  # e.g. Tiistai
if len(sys.argv) > 1:
    weekday = sys.argv[1]

pattern = re.compile('.*{}.*'.format(weekday))
URL = 'http://pompier.fi/espa/lounas/'
text = get_html(URL)
soup = BeautifulSoup(text)
# columns = soup.find_all('strong')
todays_lunch = soup.find(text=pattern)
print(todays_lunch.parent.parent.text)

from libvoikko import Voikko, Token
v = Voikko(u"fi-x-morphoid")
ttt = todays_lunch.parent.parent.text.replace('-', ' ').replace('\r', ' ').replace('\n', ' ')
all_words = []
for word in ttt.split(" "):
    word = word.strip('\n\r,.')
    foo = v.analyze(word)
    print("-- " + word + "--")
    if foo and 'BASEFORM' in foo[0]:
        base = foo[0]['BASEFORM']
    else:
        base = word
    all_words.append(base)
    print(":  " + base)


print(all_words)

for w in ['härkä', 'lohi', 'entrecote']:
    if w in all_words:
        print("POMPIERIIN: {} !".format(w))
