import  requests
import json
from datetime import  datetime
from Scripts import get_coordinates

class iss:

    def jsonresponse(self , parameters):
        try :
            response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
            return response.json()['response']
        except:
            print("Error code:"+response.status_code)


    def parsejson(self,parameters):

        passtimes = self.jsonresponse(parameters)

        risetimes = []

        for d  in passtimes:
            time = d['risetime']
            risetimes.append(time)

        times = []

        for rt in risetimes:
            time = datetime.fromtimestamp(rt)
            times.append(time)
            print(time)

coordinates = get_coordinates.getcord()
parameters = coordinates.parsecord()
issapi = iss()
issapi.parsejson(parameters)


