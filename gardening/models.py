from django.db import models
from datetime import datetime, timedelta

class GardeningTip(models.Model):
    """Model to store gardening tips related to seasons and weather."""
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    best_plants = models.CharField(max_length=500, help_text="Comma-separated list of best plants")
    tips = models.TextField(help_text="Detailed gardening tips for this season")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.get_season_display()})"
    
    class Meta:
        ordering = ['-created_at']


class WeatherForecast(models.Model):
    """Model to store weather forecast data (static or manually updated)."""
    date = models.DateField()
    day_of_week = models.CharField(max_length=10)
    temperature = models.IntegerField(help_text="Temperature in Celsius")
    condition = models.CharField(
        max_length=50,
        choices=[
            ('sunny', 'Sunny'),
            ('cloudy', 'Cloudy'),
            ('rainy', 'Rainy'),
            ('snowy', 'Snowy'),
            ('partly_cloudy', 'Partly Cloudy'),
        ]
    )
    humidity = models.IntegerField(help_text="Humidity percentage")
    wind_speed = models.IntegerField(help_text="Wind speed in km/h")
    uv_index = models.IntegerField(help_text="UV index")
    
    def __str__(self):
        return f"{self.day_of_week} - {self.temperature}°C ({self.get_condition_display()})"
    
    class Meta:
        ordering = ['date']
        unique_together = ('date',)
