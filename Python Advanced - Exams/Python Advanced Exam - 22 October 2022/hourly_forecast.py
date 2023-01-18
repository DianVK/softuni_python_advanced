def forecast(*args):
    result = ""
    forecast_all_citys = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }
    for items in args:
        city = items[0]
        weather = items[1]
        if weather == "Sunny":
            forecast_all_citys['Sunny'].append(city)
        elif weather == "Cloudy":
            forecast_all_citys['Cloudy'].append(city)
        elif weather == "Rainy":
            forecast_all_citys['Rainy'].append(city)
    forecast_all_citys['Sunny'] = sorted(forecast_all_citys['Sunny'])
    forecast_all_citys['Cloudy'] = sorted(forecast_all_citys['Cloudy'])
    forecast_all_citys['Rainy'] = sorted(forecast_all_citys['Rainy'])
    for x in forecast_all_citys['Sunny']:
        result += f"{x} - Sunny\n"
    for x in forecast_all_citys['Cloudy']:
        result += f"{x} - Cloudy\n"
    for x in forecast_all_citys['Rainy']:
        result += f"{x} - Rainy\n"
    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
