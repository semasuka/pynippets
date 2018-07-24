"""
You need to create a function that will validate if given parameters 
are valid geographical coordinates.

Valid coordinates look like the following: "23.32353342, -32.543534534". 
The return value should be either true or false.

Latitude (which is first float) can be between 0 and 90, positive or 
negative. Longitude (which is second float) can be between 0 and 180, 
positive or negative.

Coordinates can only contain digits, or one of the following symbols 
(including space after comma) -, .

There should be no space between the minus "-" sign and the digit 
after it.

Here are some valid coordinates:

-23, 25
24.53525235, 23.45235
04, -23.234235
43.91343345, 143
4, -3
And some invalid ones:

23.234, - 23.4234
2342.43536, 34.324236
N23.43345, E32.6457
99.234, 12.324
6.325624, 43.34345.345
0, 1,2
0.342q0832, 1.2324

"""
def is_valid_coordinates(coordinates):
    coordinates_list = []
    for char in coordinates:
        if char == "e":
            return False
    else:
        for coor in coordinates.split(","):

                #if coor.isdigit() or coor.isdecimal():
                try:
                    coordinates_list.append(float(coor.strip()))
                except ValueError:
                    return False
                # else:
                #     return False
        if len(coordinates_list) == 2:
            coor_loop_count = 0
            correct_coor = []
            for coor in coordinates_list:
                coor_loop_count+=1
                if coor_loop_count == 1:
                    coor = int(coor)
                    if coor in range(-90,91):
                        correct_coor.append(True)
                    else:
                        correct_coor.append(False)
                if coor_loop_count == 2:
                    coor = int(coor)
                    if coor in range(-180,181):
                        correct_coor.append(True)
                    else:
                        correct_coor.append(False)
            correct_coor = set(correct_coor)
            if len(correct_coor) == 1:
                return True
            else:
                return False
        else:
            return False



print(is_valid_coordinates("23.245, 11"))