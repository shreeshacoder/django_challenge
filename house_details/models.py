from django.db import models

# Create your models here.


class HouseDetails(models.Model):
    area_unit = models.CharField(max_length = 6)
    bathrooms = models.FloatField(null = True)
    bedrooms = models.IntegerField(null = True)
    home_size = models.IntegerField(null = True)
    home_type = models.CharField(max_length = 30, null = True)
    last_sold_date = models.DateField(null = True)
    last_sold_price = models.IntegerField(null = True)
    link = models.CharField(max_length = 2083, null = True)
    price = models.CharField(max_length = 6, null = True)
    property_size = models.IntegerField(null = True)
    rent_price = models.IntegerField(null = True)
    rentzestimate_amount = models.IntegerField(null = True)
    rentzestimate_last_updated = models.DateField(null = True)
    tax_value = models.IntegerField(null = True)
    tax_year = models.IntegerField(null = True)
    year_built = models.IntegerField(null = True)
    zestimate_amount = models.IntegerField(null = True)
    zestimate_last_updated = models.DateField(null = True)
    zillow_id = models.IntegerField()
    address =  models.CharField(max_length = 50, null = True)
    city =  models.CharField(max_length = 30, null = True)
    state =  models.CharField(max_length = 2, null = True)
    zipcode = models.IntegerField(null = True)