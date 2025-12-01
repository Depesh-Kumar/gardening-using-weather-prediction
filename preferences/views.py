# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PreferenceForm
def set_preferences(request):
    # default values
    initial = {
        'theme': request.COOKIES.get('theme', 'light'),
        'language': request.COOKIES.get('language', 'en'),
    }
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            theme = form.cleaned_data['theme']
            language = form.cleaned_data['language']
            resp = redirect(request.POST.get('next') or reverse('preferences:preference_form'))
            # set cookies — set expiry (e.g., 365 days)
            max_age = 365 * 24 * 60 * 60
            resp.set_cookie('theme', theme, max_age=max_age, httponly=False)
            resp.set_cookie('language', language, max_age=max_age, httponly=False)
            return resp
    else:
        form = PreferenceForm(initial=initial)
    return render(request, 'preferences/preference_form.html', {'form': form})
