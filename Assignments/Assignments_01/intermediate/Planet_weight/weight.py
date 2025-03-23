MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 1.06
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.19

def main():
    earth_weight = float(input("Enter your weight (kg): "))
    planet = input("Enter a planet: ")

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight) + " kg")

if __name__ == "__main__":
    main()
