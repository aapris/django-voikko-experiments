from django.shortcuts import render

from .forms import TextForm
from .voikkotools import voikko_analyze


def index(request):
    a = []
    if request.method == "POST":
        tf = TextForm(request.POST)
        if tf.is_valid():
            a = voikko_analyze(tf.cleaned_data.get("text"))
    else:
        tf = TextForm()
    return render(
        request,
        "base.html",
        {
            "textform": tf,
            "analyzed": a,
        },
    )
