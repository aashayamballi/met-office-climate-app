from django.contrib import admin
from .models import MetOfficeWeatherData


all_met_office_app_models = [MetOfficeWeatherData]
admin.site.register(all_met_office_app_models)

