# 🌟 Exercise 7 : Temperature Advice

import random

def get_random_temp(season):
    if season == "winter":
        lower_limit, upper_limit = -10, 16
    elif season == "spring":
        lower_limit, upper_limit = 0, 20
    elif season == "summer":
        lower_limit, upper_limit = 18, 40
    elif season == "autumn":
        lower_limit, upper_limit = 5, 18
    else:
        print("Invalid season!")
        return None
    
    temp = random.uniform(lower_limit, upper_limit)
    return temp

def get_temperature_advice(temp):
    if temp < 0:
        return "Brrr, that's freezing! Wear some extra layers today."
    elif 0 <= temp <= 16:
        return "Quite chilly! Don't forget your coat."
    elif 16 < temp <= 23:
        return "A little chilly, but not too bad. A light jacket will do."
    elif 24 <= temp <= 32:
        return "Nice and warm! Enjoy the weather."
    elif 32 < temp <= 40:
        return "It's hot! Make sure to stay hydrated."

def main():
    season = input("Please enter the season (winter, spring, summer, autumn): ").lower()
    
    temp = get_random_temp(season)
    
    if temp is not None:
        print(f"The temperature right now is {temp:.2f} degrees Celsius.")
        
        advice = get_temperature_advice(temp)
        print(advice)

main()
