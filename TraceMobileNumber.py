import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Use phone number as a string.
# use country code also.
# will provide timezone, carrier and region

number = input("Enter your number with country code: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print("Your input number: ",number)
print(phone)
print("Time Zone: ",time)
print("Sim company name: ",car)
print("Region: ",reg)
