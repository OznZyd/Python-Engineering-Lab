import requests

while True:
    citySelection = input("Please enter the city name")
    if citySelection.isdigit():
        print("Please enter the valid city")
    else:
        try:
            url = f"https://wttr.in/{citySelection}?format=j1"
            answer = requests.get(url)
            value = answer.json()
            feelsLike = value['current_condition'][0]['FeelsLikeC']
            temperature = value['current_condition'][0]['temp_C']
            print(f'{citySelection} icin hava durumu {temperature} C')
            print(f'Feels Like : {feelsLike} C')
            break
        except KeyError:
            print("City Not found, PLease try again")




