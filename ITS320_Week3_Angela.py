# Python project accepting user input on weather conditions and displaying 
# wardrobe suggestions based on the input.

# Prompt user to enter the temperature value in Fahrenheit
temperature = int(input("Please enter temperature in Fahrenheit (Example - 86): "))

# Validate user input to ensure it is within the correct range 
if temperature < -129 or temperature > 134:
    print("Error: Temperature must be between -129 and 134 degrees Fahrenheit.")
    temperature = int(input("Please enter temperature in Fahrenheit (Example - 86): "))  # Reprompt for user input

# Prompt user to enter wind speed in miles per hour
wind_speed = int(input("Please enter wind speed in miles per hour (Example - 10): "))

# Validate user input to ensure it is within the correct range
if wind_speed < 0 or wind_speed > 252:
    print("Error: Wind speed must be between 0 and 252 miles per hour.")
    wind_speed = int(input("Please enter wind speed in miles per hour (Example - 10): "))  # Reprompt for user input

# Prompt user to enter the weather type (sunny, cloudy, rainy, snowy)
weather_type = input("Please enter the weather type (sunny, cloudy, rainy, snowy): ".lower())

# Validate user input to ensure it is a valid weather type
if weather_type not in ["sunny", "cloudy", "rainy", "snowy"]:
    print("Error: Weather type must be one of the following: sunny, cloudy, rainy, snowy.")
    weather_type = input("Please enter the weather type (sunny, cloudy, rainy, snowy): ".lower())  # Reprompt for user input

#




# REFERENCES
# 1. GeeksforGeeks. (2026, July 27). "String lower() Method in Python" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-string-lower/
#
# 2. GeeksforGeeks. (2026, June 16). "Python Lists" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-lists/