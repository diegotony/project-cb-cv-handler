import json
import requests



URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/"


def get_data(endpoint, group):
    try:
        response = requests.get(
            URL+endpoint,
        )
        
        json_response = json.loads(response.text)
        return json_response['_embedded'][group]
    except Exception as e:
        return {"error": e}
