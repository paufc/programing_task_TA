g = 9.81 # gravity [m/s^2]

# Aerodynamic parameters
b = 17      # span [m]
S = 27      # wing surface [m^2]
m = 5100    # total mass [kg]
fuelPercentatge = 0.2 # fuel percentage
fuelMass = m * fuelPercentatge # fuel mass [kg]
CL0 = 0.12  # lift coefficient at α = 0
CLAlpha = 0.09  # lift coefficient slope
alphaS = 14.2   # stall angle [deg]
CD0 = 0.019 # drag coefficient at α = 0
k = 0.11    # drag coefficient slope

def getCL(alpha):
    global CL0, CLAlpha
    return CL0 + (CLAlpha * alpha)

def getCD(alpha):
    global CD0, k
    CL = getCL(alpha)
    return CD0 + (k * (CL ** 2))

# Turbojet parameters
ThrustAvailableAtSL = 18100 # thrust at sea level [N]

def getThrust(partialPressure):
    global ThrustAvailableAtSL
    return ThrustAvailableAtSL * partialPressure

# Turboprop parameters
PowerAvailableAtSL = 1.1e6 # power at sea level [W]

def getPower(partialPressure):
    global PowerAvailableAtSL
    return PowerAvailableAtSL * partialPressure

# Flight conditions sea level
sealevel_heigth = 0 # altitude at sea level [m]
density = 1.225 # air density at sea level [kg/m^3]
temperature = 288.15 # temperature at sea level [K]

# cruise conditions
cruise_altitude = 11000 # [m]
cruise_AirDensity = density/3 # [kg/m^3]
partialDensityAtCR = cruise_AirDensity/density
cruise_temperature = 221.75 #  [K]

A = 0.5 * airDensityAtSL * S * CD0
B = 2 * k / (airDensityAtSL * S)