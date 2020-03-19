from flask import jsonify
from .commands_data import commands_list
from .api_requets import get_data
from .utils import object_data,array_data

URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/"


def prevencionTransporte():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    transporte=[]
    for i in data:
        if i['lugar'] == "transporte":
            transporte.append(object_data("text",i['manera']))
    return array_data(transporte,"lo que diga Andrr")

def prevencionHogar():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    hogar=[]
    for i in data:
        if i['lugar'] == "casa":
            hogar.append(object_data("text",i['manera']))
    return array_data(hogar,"lo que diga Andrr")

def prevencionTrabajo():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo=[]
    for i in data:
        if i['lugar'] == "trabajo":
            trabajo.append(object_data("text",i['manera']))
    return array_data(trabajo,"lo que diga Andrr")


def chProvincia():
    print("comando")
    return "oka"


def chCiudad():
    print("comando")
    return "oka"


def sintomas():
    data = get_data("sintomas", "sintomas")
    print(data)
    sintomas=[]
    # for i in data:
    #     sintomas.append(object_data("text",i['nombre']))
    # return array_data(sintomas,"lo que diga Andrr")


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
    func = switcher.get(argument, lambda: {"error":"Invalid command"})
    # Execute the function
    return func()


def get_all_commands():
    print(commands)
    return jsonify(commands_list)


def getList(dict):
    return dict.keys()




switcher = {
    "transporte": prevencionTransporte,
    "hogar": prevencionHogar,
    "trabajo": prevencionTrabajo,
    "provincia": chProvincia,
    "ciudad": chCiudad,
    "sintomas": sintomas,
    "educacion": htEducacion,
    "teletrabajo": htTeletrabajo,
    "estadoCuarentena": estadoCuarentena,
    "medios": mediosComunicacion,
    "ultimasNoticias": ultimasNoticias,
}

