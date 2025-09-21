from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews.'

    def handle(self, *args, **kwargs):
        # sample listing that willbe looped through
        listings = [
            Listing.objects.create(name=f"Listing {i}", description="Beach front House", price=10000.0, location="Mombasa")
            for i in range(1, 6)
        ]

        #sample booking
        for listing in listings:
            Booking.objects.create(listing=listing, user="John Doe", start_date="2025-01-01", end_date="2025-01-05")

        #sample booking
        bookings = Booking.objects.all()
        for booking in bookings:
            Review.objects.create(booking=booking, user="John Doe", rating=random.randint(1, 5), comment="Very Beautiful")
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the db'))
