old_position = 100 # start-posiotion
old_velocity = 0 #  initial velocity
gravity = -10 # acceleration gracity 10m/s^2
old_fuel = 100 # liters
thrusters= 0 #0~20


def inputthruster():
    thrusters = int(input("Set thrusters(0-20) : "))
    if thrusters < 0 :
        print "No thrusters(0)!"
        thrusters =0
    elif thrusters >= 20 :
        print "Thrusters at max(20)!"
        thrusters = 20
    return thrusters

def fuel(old_fuel,thrusters):
    new_fuel = old_fuel - thrusters
    if new_fuel < 0:
        print "Out of fuel! Thrusters at %d"%(old_fuel)
        thrusters = old_fuel
        new_fuel = 0
    return new_fuel,thrusters

def position(old_position,old_velocity,acceleration):
    if old_position < 0:
        return 0
    return old_position + old_velocity + acceleration * 0.5

while True:
    print "P : %3d V: %3d F: %3d" % (old_position,old_velocity,old_fuel)
    if old_fuel != 0:
        thrusters = inputthruster();
    else:
        print "No fuel -- rocket is in free-fall!"
    new_fuel, thrusters = fuel(old_fuel,thrusters)
    acceleration = gravity + thrusters
    new_position = position(old_position,old_velocity,acceleration)
    new_velocity = old_velocity+acceleration

    old_fuel = new_fuel
    old_velocity = new_velocity
    old_position = new_position

    if old_position <= 0 :
        old_position=0
        print "P : %3d V: %3d F: %3d" % (old_position, old_velocity, old_fuel)
        if old_velocity >= -3:
            print "Landing successful!"
            break
        else:
            print "Rocket crashed! Velocity was %d" % old_velocity
            break