"""
Advance Unit converter by Semasuka
"""

#print the main menu
print("Welcome to the unit converter\n\n1--Acceleration"\
      "\n2--Angle"\
      "\n3--Area"\
      "\n4--Currency"\
      "\n5--Data"\
      "\n6--Density"\
      "\n7--Electric Current"\
      "\n8--Energy"\
      "\n9--Force"\
      "\n10--Fuel Consumption"\
      "\n11--Length"\
      "\n12--Mass"\
      "\n13--Power"\
      "\n14--Pressure"\
      "\n15--Sound"\
      "\n16--Speed"\
      "\n17--Temperature"\
      "\n18--Time"\
      "\n19--Torque"\
      "\n20--Volume")

#acceleration
def acceleration():
    num = float(input("\nEnter the number\n"))
    print("\nConvert "
          ,num,
          " from\n1--Centigal"\
          "\n2--Centimeter/square second"\
          "\n3--Decigal"\
          "\n4--Meter/square second"
          "\n5--Decimeter/square second"\
          "\n6--Dekameter/square second"\
          "\n7--Foot/square second"\
          "\n8--G-unit(G)"\
          "\n9--Gal"\
          "\n10--Galeo"\
          "\n11--Gn"\
          "\n12--Grav"\
          "\n13--Hectometer/square second"\
          "\n14--Inch/square second"\
          "\n15--Kilometer/square second"\
          "\n16--Kilometer/hour second"\
          "\n17--Meter/square second"\
          "\n18--Mile/hour minute"\
          "\n19--Mile/hour second"\
          "\n20--Mile/square second"\
          "\n21--Milligal"\
          "\n22--Millimeter/square second")
    
    def switcher_func_acc(current_unit):
        """
        A function that switch(select) between different acceleration units
        """
        switcher = {
            1:centigal,
            2:centimeter_square_second,
            3:decigal,
            4:meter_square second,
            5--Decimeter/square second"\
            6--Dekameter/square second"\
            7--Foot/square second"\
            8--G-unit(G)"\
            9--Gal"\
            10--Galeo"\
            11--Gn"\
            12--Grav"\
            13--Hectometer/square second"\
            14--Inch/square second"\
            15--Kilometer/square second"\
            16--Kilometer/hour second"\
            17--Meter/square second"\
            18--Mile/hour minute"\
            19--Mile/hour second"\
            20--Mile/square second"\
            21--Milligal"\
          "\n22--Millimeter/square second"
        }
        switcher_fun = switcher.get(choice_unit)
        switcher_fun()
    
    
    choice_unit_type_correct = False
    while not choice_unit_correct:
        try:
            current_unit = int(input("\n"))
        except ValueError:
            print("\nText are not allowed, Please enter a number")
        else:
            if current_unit in range(1,23):
                choice_unit_type_correct = True
                switcher_func_acc(current_unit)
            else:
                print("\nPlease enter a number between 1 and 22")
def angle():
    pass
def area():
    pass
def currency():
    pass
def data():
    pass
def density():
    pass
def electric_current():
    pass
def energy():
    pass
def force():
    pass
def fuel_consumption():
    pass
def length():
    pass
def mass():
    pass
def power():
    pass
def pressure():
    pass
def sound():
    pass
def speed():
    pass
def temperature():
    pass
def time():
    pass
def torque():
    pass
def volume():
    pass

def switcher_fun(choice_unit):
    """
    A function that switch(select) between unit converter
    """
    switcher = {
        1:acceleration,
        2:angle,
        3:area,
        4:currency,
        5:data,
        6:density,
        7:electric_current,
        8:energy,
        9:force,
        10:fuel_consumption,
        11:length,
        12:mass,
        13:power,
        14:pressure,
        15:sound,
        16:speed,
        17:temperature,
        18:time,
        19:torque,
        20:volume
    }
    switcher_fun = switcher.get(choice_unit)
    switcher_fun()

choice_unit_correct = False
while not choice_unit_correct:
    try:
        choice_unit = int(input('\nSelect between 1 and 20\n'))
    except ValueError:
        print("\nText are not allowed, Please enter a number")
    else:
        if choice_unit in range(1,21):
            choice_unit_correct = True
            switcher_fun(choice_unit)
        else:
            print("\nPlease enter a number between 1 and 20")

        
        