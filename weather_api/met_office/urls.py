from django.urls import path
from .views import UpdateMetOfficeData

urlpatterns = [
    path('met-office-climate-data/', UpdateMetOfficeData.as_view(), 
                                                name="met_office_climate_data")
]
