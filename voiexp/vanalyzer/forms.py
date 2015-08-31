from django import forms
from django.utils.translation import ugettext_lazy as _


class TextForm(forms.Form):
    text = forms.CharField(
        max_length=10000, label=_(u'Text'), required=True,
        widget=forms.Textarea({
            'class': 'form-control',
            'placeholder': _(u"Text to analyze")}))
