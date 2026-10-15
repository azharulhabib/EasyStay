import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from e_booking_api.models import Owner, Customer, RentalListing, RentalImage, UtilityBillImage
from rest_framework.test import APIClient

owner = Owner.objects.get(email='dara@gmail.com')

# Clean up any existing listings for this owner to ensure exact 3
RentalListing.objects.filter(owner=owner).delete()

listings_data = [
    {
        'title': 'Grand Horizon Luxury Penthouse',
        'description': 'Stunning top-floor luxury penthouse with panoramic city skyline views, private terrace, designer kitchen, floor-to-ceiling windows, and private elevator access.',
        'price': 3500.00,
        'address': '740 Park Avenue',
        'city': 'New York',
        'state': 'NY',
        'home_size': 2400,
        'floor': '32nd Floor',
        'image': 'house_images/modern_apartment.jpg'
    },
    {
        'title': 'Serene Garden Suburban Villa',
        'description': 'Charming and peaceful family villa surrounded by private lush greenery, modern open-concept living area, heated pool, high-speed WiFi, and 2-car garage.',
        'price': 2200.00,
        'address': '18 Maplewood Drive',
        'city': 'Greenwich',
        'state': 'CT',
        'home_size': 3100,
        'floor': 'Ground & 1st Floor',
        'image': 'house_images/suburban_villa.jpg'
    },
    {
        'title': 'Urban Minimalist Studio Loft',
        'description': 'Sleek and sun-drenched industrial-chic studio loft located in the heart of the arts district. Features exposed brick walls, smart home automation, and close to subway.',
        'price': 1450.00,
        'address': '215 Mercer Street',
        'city': 'New York',
        'state': 'NY',
        'home_size': 850,
        'floor': '4th Floor',
        'image': 'house_images/minimalist_studio.jpg'
    }
]

created_listings = []
for data in listings_data:
    listing = RentalListing.objects.create(
        owner=owner,
        title=data['title'],
        description=data['description'],
        price=data['price'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        booking_schedule=datetime.date.today() + datetime.timedelta(days=7),
        home_size=data['home_size'],
        floor=data['floor'],
        approved='pending',
        availability_status=True
    )
    RentalImage.objects.create(listing=listing, image=data['image'])
    UtilityBillImage.objects.create(listing=listing, image='utility_bills/utility_bill_sample.jpg')
    created_listings.append(listing)
    print(f"Created listing ID {listing.id}: '{listing.title}' (Status: {listing.approved})")

print("\n--- Performing Admin Approval ---")
for listing in created_listings:
    listing.approved = 'accepted'
    listing.availability_status = True
    listing.save()
    print(f"Approved Listing ID {listing.id}: '{listing.title}' -> Status: {listing.approved}")

print("\n--- Verifying Customer View (zaza@gmail.com) ---")
client = APIClient()
login_res = client.post('/api/login/', {'email': 'zaza@gmail.com', 'password': 'Admin@123'}, format='json', HTTP_HOST='localhost:8001')
access_token = login_res.data['access']

client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
listings_res = client.get('/api/rentallistings/', HTTP_HOST='localhost:8001')
print(f"Customer sees {len(listings_res.data)} approved listings:")
for l in listings_res.data:
    print(f"  • ID {l['id']}: {l['title']} (${l['price']}/month, {l['city']}, {l['state']}) [Approved: {l['approved']}]")
