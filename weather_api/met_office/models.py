# python related
import datetime

# django related
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class MetOfficeWeatherData(models.Model):

    year = models.IntegerField("year value", validators=[MinValueValidator(1984), 
                                max_value_current_year], unique=True)
    jan = models.FloatField("January data", null=True, blank=True, default=None)
    feb = models.FloatField("February data", null=True, blank=True, default=None)
    mar = models.FloatField("March data", null=True, blank=True, default=None)
    apr = models.FloatField("April data",null=True, blank=True, default=None)
    may = models.FloatField("May data", null=True, blank=True, default=None)
    jun = models.FloatField("June data", null=True, blank=True, default=None)
    jul = models.FloatField("July data", null=True, blank=True, default=None)
    aug = models.FloatField("August data", null=True, blank=True, default=None)
    sep = models.FloatField("September data",null=True, blank=True, default=None)
    oct = models.FloatField("October data",null=True, blank=True, default=None)
    nov = models.FloatField("November data",null=True, blank=True, default=None)
    dec = models.FloatField("December data", null=True, blank=True, default=None)
    win = models.FloatField("Winter data",null=True, blank=True, default=None)
    spr = models.FloatField("Spring data",null=True, blank=True, default=None)
    sum = models.FloatField("Summer data",null=True, blank=True, default=None)
    aut = models.FloatField("Autumn data", null=True, blank=True, default=None)
    ann = models.FloatField("Ann data", null=True, blank=True, default=None)

    def __str__(self):
        return str(self.year)
