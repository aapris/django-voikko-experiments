# -*- coding: utf-8 -*-
import sys
import re

if sys.version_info > (3,):
    from libvoikko3 import Voikko, Token
    def unicode(x, enc):
        return x
else:
    from libvoikko2 import Voikko, Token

v = Voikko(u"fi-x-morphoid")

# Read file contents
fname = sys.argv[1]
with open(fname, 'rt') as f:
    text = f.read()

# Replace all punctuation characters with space
ws_replace = re.compile('[\-\r\n\.,]')
text = ws_replace.sub(' ', text)
words = text.split(' ')
# Strip spaces
words = [x.strip() for x in words]
# Remove empty items
words = filter(None, words)
# Transform to unicode when using python2
words = [unicode(x, 'utf8') for x in words]

# Loop all words and analyze them
for word in words:
    aword = v.analyze(word)
    i = 0
    if aword:
        for f in aword:
            i += 1
            if 'BASEFORM' in f:
                base = f['BASEFORM']
                print(u'{:<30} {:<30} {} -- {}'.format(base, word, i, f['CLASS']))
                print(aword)
    else:
        base = word
        print(base + ' -- NOT FOUND')
