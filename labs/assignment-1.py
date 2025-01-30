# Assignment #1 - Temperature, Speed, and Distance

# Function convert Celsius to Fahrenheit
def temp_convert(celsius):
    """Convert temperature. Celsius to Fahrenheit."""
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Run assignment code
if __name__ == "__main__":
    # Task 1: Conversion tempatures
    celsius_temp = float(input("Enter the temperature in Celsius: "))
    fahrenheit_temp = temp_convert(celsius_temp)
    print(f"The temperature {celsius_temp}°C converted to Fahrenheit is {fahrenheit_temp}°F.")

    # Task 2: Distance light takes to travel from Sun to Earth
    speed_of_light = 186000  # miles/second
    distance_sun_to_earth = 93000000  # miles

    time_in_seconds = distance_sun_to_earth / speed_of_light
    print(f"Light takes approximately {time_in_seconds:.2f} seconds to travel from the Sun to Earth.")


# References:
"""
- Google: Google.com
- OpenAI: ChatGPT
"""
