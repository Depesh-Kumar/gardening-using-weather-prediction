# 🌿 Gardening Tips & Weather Prediction System

A Django-based web application for gardening enthusiasts that combines gardening tips with static weather forecasts to help plan gardening activities throughout the year.

## Features

- **🌱 Seasonal Gardening Tips**: Curated gardening advice for Spring, Summer, Fall, and Winter
- **📊 7-Day Weather Forecast**: Static weather data with temperature, humidity, wind speed, and UV index
- **📍 Current Weather Display**: Quick view of today's weather conditions
- **🌍 Seasonal Calendar**: Overview of what to do in each season
- **🎯 Plant Recommendations**: Best plants for each season
- **💡 Weather-Based Gardening Tips**: Contextual advice based on weather conditions
- **🎨 Responsive Design**: Mobile-friendly interface with a green theme

## Project Structure

```
mysite/
├── gardening/              # Main gardening app
│   ├── migrations/         # Database migrations
│   ├── models.py           # GardeningTip & WeatherForecast models
│   ├── views.py            # Views for all pages
│   ├── urls.py             # URL routing
│   ├── admin.py            # Django admin configuration
│   └── apps.py             # App configuration
├── preferences/            # User preferences app
│   ├── forms.py            # Preference form
│   ├── views.py            # Preference view
│   └── urls.py             # Preference URLs
├── mysite/                 # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── templates/              # HTML templates
│   ├── gardening_base.html # Base template with navigation
│   └── gardening/
│       ├── home.html       # Home page with current weather & tips
│       ├── weather_forecast.html  # Detailed forecast
│       ├── tips_list.html  # All gardening tips
│       └── tip_detail.html # Individual tip details
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── README.md               # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 5.2.6

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gardening-weather-prediction.git
cd gardening-weather-prediction
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django==5.2.6
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Main Pages

1. **Home** (`/gardening/`)
   - Displays current weather and 7-day forecast
   - Shows seasonal gardening tips
   - Quick links to weather and tips pages

2. **Weather Forecast** (`/gardening/weather/`)
   - Detailed 7-day forecast
   - Weather conditions with icons
   - Gardening advice based on weather
   - Weather conditions guide

3. **Gardening Tips** (`/gardening/tips/`)
   - All gardening tips organized by season
   - Seasonal calendar overview
   - Best plants for each season

4. **Tip Details** (`/gardening/tips/<id>/`)
   - Detailed view of individual tips
   - Seasonal information
   - Step-by-step gardening instructions

5. **Preferences** (`/preferences/`)
   - Theme selection (Light/Dark)
   - Language preference (English/Hindi)
   - Settings saved as cookies

## Models

### GardeningTip
- `title`: Tip title
- `description`: Short description
- `season`: Spring, Summer, Fall, Winter
- `best_plants`: Recommended plants
- `tips`: Detailed gardening instructions
- `created_at`: Creation timestamp

### WeatherForecast
- `date`: Forecast date
- `day_of_week`: Day name
- `temperature`: Temperature in Celsius
- `condition`: Weather condition
- `humidity`: Humidity percentage
- `wind_speed`: Wind speed in km/h
- `uv_index`: UV index value

## Adding Data

### Via Django Admin
1. Start the server: `python manage.py runserver`
2. Go to `http://127.0.0.1:8000/admin/`
3. Login with your superuser credentials
4. Add GardeningTips and WeatherForecasts directly

### Via Django Shell
```bash
python manage.py shell
from gardening.models import GardeningTip, WeatherForecast
from datetime import date

# Add a gardening tip
tip = GardeningTip.objects.create(
    title="Spring Planting",
    description="Best practices for spring gardening",
    season="spring",
    best_plants="Tomatoes, Lettuce, Peas",
    tips="Water regularly and mulch the beds."
)

# Add weather forecast
weather = WeatherForecast.objects.create(
    date=date.today(),
    day_of_week="Monday",
    temperature=22,
    condition="sunny",
    humidity=65,
    wind_speed=10,
    uv_index=6
)
```

## Static Data

The application includes hardcoded fallback data in `views.py`:
- Default 7-day forecast if the database is empty
- Seasonal gardening tips for all seasons
- Weather-based gardening advice

## Customization

### Theme Colors
Edit the CSS in `templates/gardening_base.html` to change the color scheme:
- Primary green: `#2d5016`
- Secondary green: `#4a7c2c`

### Add More Seasons or Weather Conditions
1. Update the model choices in `gardening/models.py`
2. Create a migration: `python manage.py makemigrations`
3. Apply it: `python manage.py migrate`
4. Add new data in admin or shell

### Integrate Real Weather API
Replace the `get_static_weather_forecast()` function in `views.py` with API calls to OpenWeatherMap, WeatherAPI, or similar services.

## Technologies Used

- **Django 5.2.6**: Web framework
- **Python 3.x**: Programming language
- **SQLite**: Database
- **HTML5 & CSS3**: Frontend
- **Django Templates**: Templating engine

## Future Enhancements

- [ ] Integrate real-time weather API (OpenWeatherMap, WeatherAPI)
- [ ] Add user authentication and personal gardens
- [ ] Implement plant care tracking and notifications
- [ ] Add photo gallery for gardening progress
- [ ] Create mobile app (React Native/Flutter)
- [ ] Add search and filtering for tips
- [ ] Implement user ratings and comments
- [ ] Add weather alerts
- [ ] Integrate soil moisture sensors

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Locked
Delete `db.sqlite3` and run migrations again:
```bash
python manage.py migrate
```

### Static Files Not Loading
Collect static files:
```bash
python manage.py collectstatic
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contact

For questions or feedback, please open an issue on GitHub or contact the project maintainers.

---

Happy Gardening! 🌿🌻🌱
