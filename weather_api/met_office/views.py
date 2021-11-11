
# python related
from typing import Union
import re

# django related
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# third party libraries
import requests

# project related
from .models import MetOfficeWeatherData
from .serializers import MetOfficeWeatherDataSerializer

class UpdateMetOfficeData(APIView):
    """
        An API to fetch the the met office climate data.

        1. get method will return the met office data stored in the db
        2. post method will update create the data based on the year
    """
    def return_float_or_none(self, value: str) -> Union[None, float]:
        """
            function that checks wheather the passed string is empty or a 
            floating value. 

            1. if empty or not a floating value then it will return None
            2. if not empty it will convert the string to float and return 
        """
        value = value.strip()
        try:
            if value:
                return float(value)
            else:
                return None
        except ValueError:
            return None
        except Exception:
            return None
    
    def get(self, request):
        """
            This method returns all the met office data stored in the DB in a 
            json format
        """
        climate_data = MetOfficeWeatherData.objects.all()
        return Response(
            MetOfficeWeatherDataSerializer(climate_data, many=True).data
        )

    def post(self, request):
        """
            This method is to update / create a year record in the database
        """
        try:
            r = requests.get(
                'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt')
            years_data = r.text.split('\n', 6)[6].split('\n')
            
            for year in years_data:
                # first four characters will always be year
                year_value_str = year[:4]

                # 4 to 89 character will be year data and always seperated 
                # by 7 spaces
                year_data_str = year[4:89]

                # 88th to end of the line will always be season data 
                # seperated by 9 spaces
                season_data_str = year[88:]

                # stripping the year data
                year = year_value_str.strip()

                # month data yealry by splitting with 7 spaces
                year_list = re.findall('.......', year_data_str)

                # season data of an year by splitting with 8 spaces 
                season_list = re.findall('........', season_data_str)

                if len(year) != 0: 
                    MetOfficeWeatherData.objects.update_or_create(
                        year=int(year), defaults={
                            "jan" : self.return_float_or_none(year_list[0]),
                            "feb":self.return_float_or_none(year_list[1]),
                            "mar": self.return_float_or_none(year_list[2]),
                            "apr": self.return_float_or_none(year_list[3]),
                            "may": self.return_float_or_none(year_list[4]),
                            "jun": self.return_float_or_none(year_list[5]),
                            "jul": self.return_float_or_none(year_list[6]),
                            "aug": self.return_float_or_none(year_list[7]),
                            "sep": self.return_float_or_none(year_list[8]),
                            "oct": self.return_float_or_none(year_list[9]),
                            "nov": self.return_float_or_none(year_list[10]),
                            "dec": self.return_float_or_none(year_list[11]),
                            "win": self.return_float_or_none(season_list[0]),
                            "spr": self.return_float_or_none(season_list[1]),
                            "sum": self.return_float_or_none(season_list[2]),
                            "aut": self.return_float_or_none(season_list[3]),
                            "ann": self.return_float_or_none(season_list[4])
                        }
                    )
        except Exception as e:
            print(e)
            return Response("Error occured while updating the met office data"
            , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Data updated successfully")

