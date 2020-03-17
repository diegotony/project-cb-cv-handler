from flask import jsonify
import json
import requests


def prevencionTransporte():
    print("comando")
    return get_data()


def prevencionHogar():
    print("comando")
    return get_data()



def prevencionTrabajo():
    print("comando")
    return get_data()



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
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func()


def get_all_commands():
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
    lista = getList(switcher)
    commands = [i for i in lista]
    print(commands)
    return jsonify(commands)


def getList(dict):
    return dict.keys()


def get_data():
    response = requests.get(
        'http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/cuidados',

    )
    json_response = json.loads(response.text)

    return  json_response['_embedded']['cuidados']
