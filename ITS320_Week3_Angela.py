# Python project accepting user input on weather conditions and displaying 
# wardrobe suggestions based on the input.

# Prompt user to enter the temperature value in Fahrenheit
temperature = int(input("Please enter temperature in Fahrenheit (Range -129 - +134; normal is 72): "))

# Validate user input to ensure it is within the correct range 
if temperature < -129 or temperature > 134:
    print("Error: Temperature must be between -129 and 134 degrees Fahrenheit.")
    temperature = int(input("Please enter temperature in Fahrenheit (Range -129 - +134; normal is 72): "))  # Reprompt for user input

# Prompt user to enter wind speed in miles per hour
wind_speed = int(input("Please enter wind speed in miles per hour (Range 0 - 252 mph; normal is 2): "))

# Validate user input to ensure it is within the correct range
if wind_speed < 0 or wind_speed > 252:
    print("Error: Wind speed must be between 0 and 252 miles per hour.")
    wind_speed = int(input("Please enter wind speed in miles per hour (Range 0 - 252 mph; normal is 2): "))  # Reprompt for user input

# Prompt user to enter the weather type (sunny, cloudy, rainy, snowy)
weather_type = input("Please enter the weather type (sunny, cloudy, rainy, snowy): ").lower()

# Validate user input to ensure it is a valid weather type
if weather_type not in ["sunny", "rainy", "snowy"]:
    print("Error: Weather type must be one of the following: sunny, rainy, snowy.")
    weather_type = input("Please enter the weather type (sunny, rainy, snowy): ").lower()  # Reprompt for user input

# Make outfit suggestion based on the weather input details
if -129 <= temperature <= 40 and 20 <= wind_speed <= 50 and weather_type == "snowy":
    print("It is very cold and windy. You should wear a heavy coat, scarf, gloves, and boots.")
elif 41 <= temperature <= 60 and 10 <= wind_speed < 20 and weather_type == "rainy":
    print("It is cool and rainy. You should wear a long sleeve shirt, pants, raincoat, waterproof shoes, and carry an umbrella.")
elif 61 <= temperature <= 80 and wind_speed < 10 and weather_type == "sunny":
    print("It is warm and sunny. You should wear a t-shirt, shorts, sandals, and sunglasses.")
else:
    print("The weather conditions are unusual. Please check the input values and try again.")




# REFERENCES
# 1. GeeksforGeeks. (2026, July 27). "String lower() Method in Python" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-string-lower/
#
# 2. GeeksforGeeks. (2026, June 16). "Python Lists" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-lists/