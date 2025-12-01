from django.shortcuts import render
from datetime import datetime, timedelta
from .models import GardeningTip, WeatherForecast
def gardening_home(request):
    """Display gardening home page with current weather and tips."""
    today = datetime.now().date()
    weather_forecasts = WeatherForecast.objects.filter(date__gte=today).order_by('date')[:7]
    if not weather_forecasts:
        weather_forecasts = get_static_weather_forecast()
    current_month = datetime.now().month
    if current_month in [3, 4, 5]:
        season = 'spring'
    elif current_month in [6, 7, 8]:
        season = 'summer'
    elif current_month in [9, 10, 11]:
        season = 'fall'
    else:
        season = 'winter'  
    tips = GardeningTip.objects.filter(season=season)
    if not tips:
        tips = get_static_gardening_tips(season)  
    context = {
        'current_weather': weather_forecasts[0] if weather_forecasts else None,
        'forecast': weather_forecasts[1:] if len(weather_forecasts) > 1 else [],
        'tips': tips,
        'season': season,
    }
    return render(request, 'gardening/home.html', context)


def weather_forecast(request):
    """Display detailed weather forecast for the next 7 days."""
    today = datetime.now().date()
    forecasts = WeatherForecast.objects.filter(date__gte=today).order_by('date')[:7]
    
    if not forecasts:
        forecasts = get_static_weather_forecast()
    
    context = {'forecasts': forecasts}
    return render(request, 'gardening/weather_forecast.html', context)


def gardening_tips(request):
    """Display all gardening tips organized by season."""
    tips = GardeningTip.objects.all()
    if not tips:
        tips = get_all_static_tips()
    
    context = {'tips': tips}
    return render(request, 'gardening/tips_list.html', context)


def gardening_tip_detail(request, tip_id):
    """Display detailed view of a single gardening tip."""
    try:
        tip = GardeningTip.objects.get(id=tip_id)
    except GardeningTip.DoesNotExist:
        # Fallback to static data if not found
        tip = None
    
    context = {'tip': tip}
    return render(request, 'gardening/tip_detail.html', context)


# Static data fallback functions
def get_static_weather_forecast():
    """Return static weather forecast data."""
    today = datetime.now().date()
    forecast_data = [
        {
            'date': today,
            'day_of_week': 'Today',
            'temperature': 22,
            'condition': 'Sunny',
            'condition_code': 'sunny',
            'humidity': 65,
            'wind_speed': 10,
            'uv_index': 6,
        },
        {
            'date': today + timedelta(days=1),
            'day_of_week': 'Tomorrow',
            'temperature': 20,
            'condition': 'Partly Cloudy',
            'condition_code': 'partly_cloudy',
            'humidity': 70,
            'wind_speed': 12,
            'uv_index': 5,
        },
        {
            'date': today + timedelta(days=2),
            'day_of_week': 'Wednesday',
            'temperature': 18,
            'condition': 'Rainy',
            'condition_code': 'rainy',
            'humidity': 85,
            'wind_speed': 15,
            'uv_index': 2,
        },
        {
            'date': today + timedelta(days=3),
            'day_of_week': 'Thursday',
            'temperature': 19,
            'condition': 'Cloudy',
            'condition_code': 'cloudy',
            'humidity': 75,
            'wind_speed': 8,
            'uv_index': 3,
        },
        {
            'date': today + timedelta(days=4),
            'day_of_week': 'Friday',
            'temperature': 23,
            'condition': 'Sunny',
            'condition_code': 'sunny',
            'humidity': 60,
            'wind_speed': 7,
            'uv_index': 7,
        },
        {
            'date': today + timedelta(days=5),
            'day_of_week': 'Saturday',
            'temperature': 25,
            'condition': 'Sunny',
            'condition_code': 'sunny',
            'humidity': 55,
            'wind_speed': 5,
            'uv_index': 8,
        },
        {
            'date': today + timedelta(days=6),
            'day_of_week': 'Sunday',
            'temperature': 21,
            'condition': 'Partly Cloudy',
            'condition_code': 'partly_cloudy',
            'humidity': 68,
            'wind_speed': 9,
            'uv_index': 4,
        },
    ]
    return forecast_data


def get_static_gardening_tips(season):
    """Return static gardening tips for a given season."""
    tips_by_season = {
        'spring': [
            {
                'id': 1,
                'title': 'Spring Gardening Guide',
                'description': 'Prepare your garden for the growing season.',
                'season': 'spring',
                'best_plants': 'Tomatoes, Lettuce, Peas, Beans, Carrots',
                'tips': '''
                - Start seeds indoors 6-8 weeks before last frost
                - Prepare soil with compost and organic matter
                - Install drip irrigation systems
                - Prune winter damage from perennials
                - Plant cool-season crops early
                - Water regularly as temperatures rise
                '''
            },
        ],
        'summer': [
            {
                'id': 2,
                'title': 'Summer Gardening Guide',
                'description': 'Keep your garden thriving in hot weather.',
                'season': 'summer',
                'best_plants': 'Tomatoes, Basil, Cucumbers, Zucchini, Peppers',
                'tips': '''
                - Water deeply and frequently, especially in hot spells
                - Mulch around plants to retain moisture
                - Provide shade for sensitive plants
                - Deadhead flowers to encourage blooming
                - Watch for pests and diseases
                - Harvest regularly to promote productivity
                '''
            },
        ],
        'fall': [
            {
                'id': 3,
                'title': 'Fall Gardening Guide',
                'description': 'Plant for autumn harvests and prepare for winter.',
                'season': 'fall',
                'best_plants': 'Kale, Broccoli, Spinach, Garlic, Mushrooms',
                'tips': '''
                - Plant cool-season crops in late summer
                - Clean up fallen leaves to prevent disease
                - Plant spring bulbs (tulips, daffodils)
                - Divide perennials
                - Apply fall fertilizer to lawns
                - Prepare beds for winter
                '''
            },
        ],
        'winter': [
            {
                'id': 4,
                'title': 'Winter Gardening Guide',
                'description': 'Maintain your garden during cold months.',
                'season': 'winter',
                'best_plants': 'Evergreens, Winter Vegetables, Hellebores',
                'tips': '''
                - Protect plants with frost cloth
                - Reduce watering as growth slows
                - Feed birds to support local wildlife
                - Plan next year's garden layout
                - Maintain garden tools and equipment
                - Monitor for winter pests
                '''
            },
        ],
    }
    return tips_by_season.get(season, [])


def get_all_static_tips():
    """Return all static gardening tips."""
    all_tips = []
    for season in ['spring', 'summer', 'fall', 'winter']:
        all_tips.extend(get_static_gardening_tips(season))
    return all_tips
