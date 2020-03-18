from flask import jsonify
import json
import requests

from .commands_data import commands_list
URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/"


def prevencionTransporte():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    return data['transporte']


def prevencionHogar():
    print("comando")


def prevencionTrabajo():
    print("comando")


def chProvincia():
    print("comando")
    return "oka"


def chCiudad():
    print("comando")
    return "oka"


def sintomas():
    print("comando")
    return "oka"


def htEducacion():
    print("comando")
    return "oka"


def htTeletrabajo():
    print("comando")


def estadoCuarentena():
    print("comando")
    return "oka"


def mediosComunicacion():
    print("comando")
    return "oka"


def ultimasNoticias():
    print("comando")
    return "oka"


def commands(argument):
    func = switcher.get(argument, lambda: "Invalid command")
    # Execute the function
    return func()


def get_all_commands():

    # lista = getList(switcher)
    # commands = [i for i in lista]
    print(commands)
    return jsonify(commands_list)


def getList(dict):
    return dict.keys()


def get_data(endpoint, group):
    response = requests.get(
        URL+endpoint,
    )
    json_response = json.loads(response.text)

    return json_response['_embedded'][group]



switcher = {
    "PrevencionTransporte": prevencionTransporte,
    "PrevencionHogar": prevencionHogar,
    "PrevencionTrabajo": prevencionTrabajo,
    "CHProvincia": chProvincia,
    "CHCiudad": chCiudad,
    "sintomas": sintomas,
    "HTEducacion": htEducacion,
    "HTTeletrabajo": htTeletrabajo,
    "estadoCuarentena": estadoCuarentena,
    "MediosComunicacion": mediosComunicacion,
    "UltimasNoticias": ultimasNoticias,
}
