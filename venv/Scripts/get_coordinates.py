import requests

class getcord:

    def __init__(self):
        print("Put a name of the city")

    def cord(self):
        place = input()
        key = 'ddc3411379994cebb18e64a92794056d' #key form opencagedata (use your own)
        #connecting with opencagedata API and getting a JSON
        try:
            response = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+place+"&key="+key)
            return response.json()['results']
        except:
            print("Error code:"+response.status_code)

    def parsecord(self):
        #Get a JSON from API with only results area
        placecord = self.cord()

        places = []
        #Getting all of the coordinates from geomatry
        for i  in placecord:
            place = i['geometry']
            places.append(place)
        #Adding to a dict parameters first coordinates from JSON
        parameters = {
            "lat": places[0]['lat'],
            "lon": places[0]['lng']
        }

        return parameters
