from django.db import models

status = {
    "APPROVED" : "APPROVED",
    "REQUESTED" : "REQUESTED",
    "SUSPEND" : "SUSPEND",
    "EXPIRED" : "EXPIRED"
}

class Food(models.Model):
    item = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.item

class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

class FoodTruck(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    permit = models.CharField(max_length=50, blank=False, null=False)
    cnn = models.CharField(max_length=20, blank=True, null=True)
    facility_type = models.CharField(max_length=20, blank=True, null=True)
    food_items = models.ForeignKey(Food, related_name='foods', blank=False, null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=status, blank=False, null=False)
    approved_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    working_hours = models.CharField(max_length=20, blank=True, null=True)
    current_location = models.ForeignKey(Coordinates, related_name='current_coordinates', blank=False, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Location(models.Model):
    location_id = models.IntegerField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    block_lot = models.CharField(max_length=10, blank=True, null=True)
    block = models.CharField(max_length=10, blank=True, null=True)
    lot = models.CharField(max_length=10, blank=True, null=True)
    fire_prevention_district = models.IntegerField(blank=True, null=True)
    police_district = models.IntegerField(blank=True, null=True)
    supervisor_district = models.IntegerField(blank=True, null=True)
    neighbourhood = models.IntegerField(blank=True, null=True)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
