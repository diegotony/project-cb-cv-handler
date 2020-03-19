from flask import jsonify
from .commands_data import commands_list
from .api_requets import get_data
from .utils import object_data

URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/"


def prevencionTransporte():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo=[]
    for i in data:
        if i['lugar'] == "transporte":
            trabajo.append(object_data("text",i['manera'],"nope"))
    return trabajo

def prevencionHogar():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo=[]
    for i in data:
        if i['lugar'] == "casa":
            trabajo.append(object_data("text",i['manera'],"nope"))
    return trabajo

def prevencionTrabajo():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo=[]
    for i in data:
        if i['lugar'] == "trabajo":
            trabajo.append(object_data("text",i['manera'],"nope"))
    return trabajo


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
    print(commands)
    return jsonify(commands_list)


def getList(dict):
    return dict.keys()




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

