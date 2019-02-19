from import_export import resources
from .models import HouseDetails

class HouseDetailsResource(resources.ModelResource):
    class Meta:
        model = HouseDetails