import  requests
import json
from datetime import  datetime
from Scripts import get_coordinates

class iss:

    def jsonresponse(self , parameters):
        #connect to api with coordinates sent
        #if a connection is failed then it show error code
        try :
            response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
            return response.json()['response']
        except:
            print("Error code:"+response.status_code)


    def parsejson(self,parameters):
        # get json from API
        passtimes = self.jsonresponse(parameters)
        #creating a table to put area from risetime section from json
        risetimes = []

        for d  in passtimes:
            time = d['risetime']
            risetimes.append(time)

        times = []
        #change format of date
        for rt in risetimes:
            time = datetime.fromtimestamp(rt)
            times.append(time)
            print(time)

#initialize get_coordinates.py class
coordinates = get_coordinates.getcord()
#Get coordinates from the city using opencagedata API and assign the result  to parameters
parameters = coordinates.parsecord()
#initialize iss class
issapi = iss()
#Init a parsejson function to get a final dates
issapi.parsejson(parameters)


