from django.shortcuts import render
from rest_framework import generics

from .models import HouseDetails
from .serializers import HouseDetailsSerializer
from tablib import Dataset


class HouseDetailsList(generics.ListAPIView):
    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer
    """
    HELLO
    """

class HouseDetailsDetail(generics.RetrieveAPIView):
    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer
    """
    HELLO
    """

class CreateHouseDetailEntry(generics.CreateAPIView):
    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer
    """
    HELLO
    """

def simple_upload(request):
    if request.method == 'POST':
        house_details_resource = HouseDetailsResource()
        dataset = Dataset()
        house_details = request.FILES['myfile']

        imported_data = dataset.load(house_details.read())
        result = house_details_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            house_details_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')