import phonenumbers
from test import number

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier

provide_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(provide_number, "en"))

phone_numbers = phonenumbers.parse(number)
valid = phonenumbers.is_valid_number(phone_numbers)
possible = phonenumbers.is_possible_number(phone_numbers)

print(valid)
print(possible)
















