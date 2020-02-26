import  requests
import json
from datetime import  datetime

class iss:

    def getparams(self):
        print("write a latitude for wanted position")
        latitude = input()
        print("write a longitude for wanted position")
        longitude = input()

        parameters = {
            "lat": latitude,
            "lon": longitude
        }
        return parameters

    def jsonresponse(self , parameters):
        try :
            response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
            print(response.status_code)
            return response.json()['response']
        except:
            print("failed to connect with api")


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


issapi = iss()
parameters = issapi.getparams()
issapi.parsejson(parameters)


