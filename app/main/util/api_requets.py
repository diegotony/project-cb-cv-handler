import json
import requests

URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/"

def get_data(endpoint, group):
    response = requests.get(
        URL+endpoint,
    )
    json_response = json.loads(response.text)
    print(json_response)
    return json_response['_embedded'][group]
