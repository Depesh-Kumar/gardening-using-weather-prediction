from django import forms
THEME_CHOICES = [
    ('light', 'Light'),
    ('dark', 'Dark'),
]
LANG_CHOICES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
]

class PreferenceForm(forms.Form):
    theme = forms.ChoiceField(choices=THEME_CHOICES, widget=forms.RadioSelect)
    language = forms.ChoiceField(choices=LANG_CHOICES)
