# from django.shortcuts import render

import sys
import re

# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import TextForm

if sys.version_info > (3,):
    from .libvoikko3 import Voikko, Token
    def unicode(x, enc):
        return x
else:
    from .libvoikko2 import Voikko, Token

v = Voikko(u'fi-x-morphoid')

def voikko_analyze(text):
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
    analyzed = []
    for word in words:
        aword = v.analyze(word)
        i = 0
        if aword:
            for f in aword:
                f['found'] = True
                f['original'] = word
                analyzed.append(f)
                # i += 1
                # if 'BASEFORM' in f:
                #     base = f['BASEFORM']
                #     print(u'{:<30} {:<30} {} -- {}'.format(base, word, i, f['CLASS']))
                base = f['BASEFORM']
                # print(u'{:<30} {:<30} {} -- {}'.format(base, word, i, f['CLASS']))
                # print(f)
        else:
            analyzed.append({'BASEFORM': word, 'found': False, 'original': word})
            base = word
            # print(base + ' -- NOT FOUND')
    return analyzed


def index(request):
    a = []
    if request.method == 'POST':
        tf = TextForm(request.POST)
        if tf.is_valid():
            a = voikko_analyze(tf.cleaned_data.get('text'))
    else:
        tf = TextForm()
    return render_to_response(
        'base.html', {
            'textform': tf,
            'analyzed': a,
        },
        context_instance=RequestContext(request),
    )
