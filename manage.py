#!/usr/bin/env python
import os
import sys
import csv

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_application.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # path = "./"
    # os.chdir(path)
    # with open("challenge_data.csv") as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         house_entry = HouseDetails.objects.create()
    #         # house_entry = HouseDetails(area_unit = row[area_unit],
    #         # bathrooms = row[bathrooms],
    #         # bedrooms = row[bedrooms],
    #         # home_size = row[home_size],
    #         # last_sold_date = row[last_sold_date],
    #         # last_sold_price = row[last_sold_price],
    #         # link = row[link],
    #         # price = row[price],
    #         # property_size = row[property_size],
    #         # rent_price = row[rent_price],
    #         # rent_estimate_amount = row[rentzestimate_amount],
    #         # rent_estimate_last_updated = row[rentzestimate_last_updated],
    #         # tax_value = row[tax_value],
    #         # tax_year = row[tax_year],
    #         # year_built = row[year_built],
    #         # zestimate_amount = row[zestimate_amount],
    #         # zestimate_last_updated = row[zestimate_last_updated],
    #         # zillow_id = row[zillow_id],
    #         # address = row[address],
    #         # city = row[city],
    #         # state = row[state],
    #         # zipcode = row[zipcode]
    #         # )
    #         house_entry.save()
    execute_from_command_line(sys.argv)
