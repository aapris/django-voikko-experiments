# from django.shortcuts import render

import sys
import re

# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import TextForm
from .voikkotools import voikko_analyze


def index(request):
    a = []
    if request.method == 'POST':
        tf = TextForm(request.POST)
        if tf.is_valid():
            a = voikko_analyze(tf.cleaned_data.get('text'))
            # for b in a:
            #     print(b)
    else:
        tf = TextForm()
    return render_to_response(
        'base.html', {
            'textform': tf,
            'analyzed': a,
        },
        context_instance=RequestContext(request),
    )
