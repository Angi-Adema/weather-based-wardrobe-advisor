# Python project accepting user input on weather conditions and displaying 
# wardrobe suggestions based on the input.

# Prompt user to enter the temperature value in Fahrenheit
temperature = int(input("Please enter temperature in Fahrenheit (Range -129 - +134; normal is 72): "))

# Validate user input to ensure it is within the correct range 
if temperature < -129 or temperature > 134:
    print("\nError: Temperature must be between -129 and 134 degrees Fahrenheit.")
    temperature = int(input("\nPlease enter temperature in Fahrenheit (Range -129 - +134; normal is 72): "))  # Reprompt for user input

# Prompt user to enter wind speed in miles per hour
wind_speed = int(input("\nPlease enter wind speed in miles per hour (Range 0 - 252 mph; normal is 2): "))

# Validate user input to ensure it is within the correct range
if wind_speed < 0 or wind_speed > 252:
    print("\nError: Wind speed must be between 0 and 252 miles per hour.")
    wind_speed = int(input("\nPlease enter wind speed in miles per hour (Range 0 - 252 mph; normal is 2): "))  # Reprompt for user input

# Prompt user to enter the weather type (sunny, cloudy, rainy, snowy)
weather_type = input("\nPlease enter the weather type (sunny, rainy, snowy): ").lower()

# Validate user input to ensure it is a valid weather type
if weather_type not in ["sunny", "rainy", "snowy"]:
    print("\nError: Weather type must be one of the following: sunny, rainy, snowy.")
    weather_type = input("\nPlease enter the weather type (sunny, rainy, snowy): ").lower()  # Reprompt for user input

# Create if-elif-else statement to make wardrobe suggestions based on the user's input
if temperature <= 40 and wind_speed >= 25 and weather_type == "snowy":
    print("\nIt is very cold and windy. Wear a heavy coat, flannel-lined pants, scarf, gloves, and boots.")
elif temperature <= 40 and 5 <= wind_speed < 25 and weather_type == "snowy":
    print("\nIt is cold and snowy. Wear a heavy coat, warm pants, gloves, and insulated boots.")
elif temperature <= 60 and wind_speed >= 20 and weather_type == "rainy":
    print("\nThe weather is cool, rainy, and windy. Wear a waterproof jacket, jeans, waterproof shoes, and carry an umbrella.")
elif temperature <= 60 and wind_speed < 20 and weather_type == "rainy":
    print("\nThe weather is cool and rainy. Wear a raincoat, long-sleeve shirt, pants, and waterproof shoes.")
elif 41 <= temperature <= 60 and wind_speed >= 15 and weather_type == "sunny":
    print("\nIt is sunny, mild, and windy. Wear a windbreaker, long-sleeve shirt, pants, and sunglasses.")
elif 41 <= temperature <= 60 and wind_speed < 15 and weather_type == "sunny":
    print("\nIt is sunny and mild. Wear a light jacket, long-sleeve shirt, jeans, and sneakers.")
elif 61 <= temperature <= 80 and wind_speed >= 10 and weather_type == "sunny":
    print("\nIt is warm and sunny but breezy. Bring a sweatshirt if needed, wear a t-shirt and jeans, secure loose clothing.")
elif 61 <= temperature <= 80 and wind_speed < 10 and weather_type == "sunny":
    print("\nIt is warm and sunny. Wear a t-shirt, jeans or shorts, and comfortable shoes.")
elif temperature > 80 and wind_speed >= 15 and weather_type == "sunny":
    print("\nIt is hot and sunny but breezy. Wear light clothing, sunglasses, and secure loose clothing.")
elif temperature > 80 and wind_speed < 15 and weather_type == "sunny":
    print("\nIt is hot and sunny. Wear a tank top, shorts, sandals, and sunglasses. Stay hydrated.")
else:
    print("\nDress comfortably and prepare for the current weather conditions.")




# REFERENCES
# 1. GeeksforGeeks. (2026, July 27). "String lower() Method in Python" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-string-lower/
#
# 2. GeeksforGeeks. (2026, June 16). "Python Lists" GeeksforGeeks.
#    https://www.geeksforgeeks.org/python/python-lists/
#
# 3. Miller, B. (n.d.). "Programming in Python 3" zyBooks, a Wiley Brand.
#    Canvas https://www.zybooks.com/