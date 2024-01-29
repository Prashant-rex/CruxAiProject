
from math import sin, cos, sqrt, atan2, radians

EARTH_RADIUS_KM = 6373.0

def calculate_distance(lat1, lon1, lat2, lon2):

    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = EARTH_RADIUS_KM * c

    return distance

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#method to get data from csv and dump to models
def import_books(file_path):
    from core.models import FoodTruck, Location, Food
    from datetime import datetime
    import csv

    date_format = '%m/%d/%Y %I:%M:%S %p'
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        # Co-ordinates Model
        for row in reader:
            try:
                coords_params = {
                    'latitude': row['Latitude'],
                    'longitude': row['Longitude']
                }
            
                location_obj, l_created = Coordinates.objects.get_or_create(**coords_params)
                if l_created:
                    location_obj.save()
                
                #Food Model
                food_params = {
                    'item': row['FoodItems']
                }

                food_obj, f_created = Food.objects.get_or_create(**food_params)
                if f_created:
                    food_obj.save()
                
                #Location Model
                location_params = {
                    'location_id': row['locationid'],
                    'description': row['LocationDescription'],
                    'address': row['Address'],
                    'block_lot': row['blocklot'],
                    'block': row['block'],
                    'lot': row['lot'],
                    'fire_prevention_district': row['Fire Prevention Districts'],
                    'police_district': row['Police Districts'],
                    'supervisor_district': row['Supervisor Districts'],
                    'neighbourhood': row['Zip Codes'],
                    'zipcode': row['Zip Codes']
                }

                Location.objects.create(**location_params)

                #FoodTruck Model
                truck_params = {
                    'name': row['Applicant'],
                    'permit': row['permit'],
                    'facility_type': row['FacilityType'],
                    'food_items': food_obj,
                    'status': row['Status'],
                    'cnn': row['cnn'],
                    'approved_date': datetime.strptime(row['Approved'], date_format),
                    'expiration_date': datetime.strptime(row['ExpirationDate'], date_format),
                    'working_hours': row['dayshours'],
                    'current_location': location_obj,

                }

                FoodTruck.objects.create(**truck_params)
            
            except:
                pass
            