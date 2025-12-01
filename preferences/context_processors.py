def preferences(request):
    # read cookies and provide defaults
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')
    return {
        'user_theme': theme,
        'user_language': language,
    }
