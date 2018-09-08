"""
A small program that generate randomly a zone and display the current time with the local time and the UTC time
"""



import pytz
import datetime
import random
import sys

the_choice = 0
places = random.sample(pytz.all_timezones,9)


print("Please select one of the following city or quit:\n")
print("0 -> To quit")

for i,place in enumerate(places,1):
    print(i,"->",place)

while the_choice not in range(1,10):
    the_choice = int(input("\nPlease select the city of your choice:\n"))
    if the_choice ==0:
        print("Quiting...")
        sys.exit()
if the_choice != 8 or the_choice != 9:
    the_choice -= 1

the_place_choosen = places[the_choice]
tz_to_display = pytz.timezone(the_place_choosen)

choosen_date = datetime.datetime.now(tz=tz_to_display).date()
choosen_time = datetime.datetime.now(tz=tz_to_display).time()
choosen_offset = datetime.datetime.now(tz=tz_to_display).utcoffset()
choosen_tz_name = datetime.datetime.now(tz=tz_to_display).tzname()
#print(choosen_offset)
local_time = datetime.datetime.now()

utc_date = datetime.datetime.utcnow().date()
utc_time = datetime.datetime.utcnow().time()
utc_offset = "0:00:00"

print("\nThe time in {} with timezone of {} is {} with an offset of {} on {}".format(the_place_choosen,choosen_tz_name,choosen_time.strftime("%H:%M:%S"),choosen_offset,choosen_date))
print("The time at your location is {}".format(local_time.strftime(" %H:%M:%S")))
print("The time at UTC is {} with an offset of {} on {}".format(utc_time.strftime("%H:%M:%S"),utc_offset,utc_date))
