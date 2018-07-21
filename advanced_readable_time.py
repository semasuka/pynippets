"""
The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""
import math
def format_duration(seconds):
    secs = 0
    mins = 0
    hrs = 0
    days = 0
    years = 0
    time_list = []
    #check if the seconds are a positive number
    if seconds > 0:
        #now
        if seconds == 0:
            return "now"
        else:
            #if the input seconds are less than a minute
            if seconds < 60:
                secs = seconds
            #if the input seconds are less than an hour
            elif seconds >=60 and seconds < 3600:
                #if no reminder in seconds modulo 60,which means that the mins are not decimal
                if not seconds%60:
                    mins = seconds/60
                elif seconds == 60:
                    secs = 0
                    mins = 1
                else:
                    #decimal part is sec and interger part is min
                    secs,mins = math.modf(seconds/60)
                        #the decimal times 60
                    secs = secs*59
            #if the input seconds are less than a day
            elif seconds >= 3600 and seconds < 86400:
                if not seconds%3600:
                    hrs = seconds/3600
                elif seconds == 3600:
                    secs = 0
                    mins = 0
                    hrs = 1
                else:
                    mins,hrs = math.modf(seconds/3600)
                    mins = mins*60
                    #print("bef mins",mins)
                    secs,mins = math.modf(mins)
                    secs = secs*59
            #if the input seconds are less than a year
            elif seconds >= 86400 and seconds < 31536000:
                if not seconds%86400:
                    days = seconds/86400
                elif seconds == 86400:
                    secs = 0
                    mins = 0
                    hrs = 0
                    days = 1
                else:
                    hrs,days = math.modf(seconds/86400)
                    hrs = hrs*24
                    mins,hrs = math.modf(hrs)
                    mins = mins*60
                    secs,mins = math.modf(mins)
                    secs = secs*59
            elif seconds >= 31536000:
                if not seconds%31536000:
                    years = seconds/31536000
                elif seconds == 31536000:
                    secs = 0
                    mins = 0
                    hrs = 0
                    days = 0
                    years = 1
                else:
                    days,years = math.modf(seconds/31536000)
                    days = days*365
                    hrs,days = math.modf(days)
                    hrs = hrs*24
                    mins,hrs = math.modf(hrs)
                    mins = mins*60
                    secs,mins = math.modf(mins)
                    secs = secs*59

            years = int(years)
            days = int(days)
            hrs = int(hrs)
            mins = int(mins)
            dec_secs = float(secs)
            if dec_secs >= 0.51:
                secs = math.ceil(float(secs))
            else:
                secs = math.floor(float(secs))
            time_list.extend((years,days,hrs,mins,secs))

            print(time_list)
            #print(formated_time(time_list))
# def formated_time(time_list):
#     years_index = 0
#     days_index = 1
#     hours_index = 2
#     mins_index = 3
#     secs_index = 4
#     final_format_time = []
#     no_zero_count = 0
#     index_list = []
#     digit_list = []

#     for digit in time_list:
#         if digit != 0:
#             no_zero_count+=1
#             index_list.append(time_list.index(digit))
#             digit_list.append(digit)
#             print(*index_list)
#             print(*digit_list)
#             #only one element is not equal to zero
#             if no_zero_count == 1:
#                 #for year
#                 if time_list.index(digit) == years_index:
#                     #one year
#                     if digit == 1:
#                         return "1 year"
#                     else:
#                         return str(digit)+" years"
#                 #for days
#                 elif time_list.index(digit) == days_index:
#                     #one day
#                     if digit == 1:
#                         return "1 day"
#                     #more than one
#                     else:
#                         return str(digit)+" days"
#                 elif time_list.index(digit) == hours_index:
#                     if digit == 1:
#                         return "1 hour"
#                     else:
#                         pass
#                 elif time_list.index(digit) == mins_index:
#                     if digit == 1:
#                         return "1 minute"
#                     else:
#                         return str(digit)+" hours"
#                 elif time_list.index(digit) == secs_index:
#                     if digit == 1:
#                         return "1 second"
#                     else:
#                         return str(digit)+" seconds"
#             elif no_zero_count == 2:
#                 for index in index_list:
#                     if index == years_index:
#                         if digit == 1:
#                             final_format_time.append("1 year")
#                         else:
#                             final_format_time.append(digit," years")
#                     elif index == days_index:
#                         pass
#                     elif index == hours_index:
#                         pass
#                     elif index == mins_index:
#                         pass
#                     elif index == secs_index:
#                         pass



format_duration(91000000)