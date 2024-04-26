import time # time
from numpy import number# number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("enter number:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(f"{phone}")
print(f"location: {time}")
print(f"internet: {car}")
print(f"country: {reg}")