from django import forms

# Form takes in input URLs from the user for the website whose articles they want to see.


class URLForm(forms.Form):
    url1 = forms.URLField(initial="https://bbc.co.uk")
    url2 = forms.URLField(initial="https://apnews.com")
    url3 = forms.URLField(initial="https://reuters.com")
