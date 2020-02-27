import requests

class getcord:

    def __init__(self):
        print("Put a name of the city")

    def cord(self):
        place = input()
        key = 'ddc3411379994cebb18e64a92794056d'
        try:
            response = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+place+"&key="+key)
            return response.json()['results']
        except:
            print("Error code:"+response.status_code)

    def parsecord(self):
        placecord = self.cord()

        places = []

        for i  in placecord:
            place = i['geometry']
            places.append(place)
        parameters = {
            "lat": places[0]['lat'],
            "lon": places[0]['lng']
        }
        return parameters
