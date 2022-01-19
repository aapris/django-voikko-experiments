from django import forms
from django.utils.translation import gettext as _


class TextForm(forms.Form):
    text = forms.CharField(
        max_length=10000,
        label=_("Text"),
        required=True,
        widget=forms.Textarea(
            {"class": "form-control", "placeholder": _("Text to analyze")}
        ),
    )
