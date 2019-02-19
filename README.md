# Django Challenge
## How to Run
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Data Modelling
The code for data modelling can be found under ```./house_details/models.py```  Null values are accepted for all fields 
except **zillow_id**  
## To ingest the CSV data
I've used [django-import-export](https://django-import-export.readthedocs.io/en/latest/) library to allow admin to 
import CSV data into the database, which can be queried later on.  
Code can for this can be found at 
