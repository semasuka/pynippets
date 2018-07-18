import math
def make_readable(seconds):
    readable_time = ""
    secs = 0
    mins = 0
    hrs = 0

    if seconds > 0 and seconds < 360000:
        if seconds < 60:
            secs = seconds
        if seconds >=60 and seconds < 3600:
            if not seconds%60:
                mins = seconds/60
            else:
                secs,mins = math.modf(seconds/60)
                secs = secs * 60
        if seconds >=3600:
            if not seconds%3600:
                hrs = seconds/3600
            else:
                mins,hrs = math.modf(seconds/3600)
                sec,mins = math.modf(mins*60)
                sec = sec*60
    print(hrs+":"+mins+":"+secs)





make_readable(2005)