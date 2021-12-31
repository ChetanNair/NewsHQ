from django import forms


class URLForm(forms.Form):
    url1 = forms.URLField(initial="https://bbc.co.uk")
    url2 = forms.URLField(initial="https://apnews.com")
    url3 = forms.URLField(initial="https://reuters.com")
