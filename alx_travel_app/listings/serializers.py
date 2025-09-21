##path the checker checks 
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'price', 'location']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date']
