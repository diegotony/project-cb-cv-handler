from flask import jsonify
from .commands_data import commands_list
from .api_requets import get_data
from .utils import  object_answer, array_answer, object_data_noticia


def prevencionTransporte():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    transporte = []
    for i in data:
        if i['lugar'] == "transporte":
            transporte.append(object_answer("text", i['manera']))
    return array_answer(transporte, "lo que diga Andrr")


def prevencionHogar():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    hogar = []
    for i in data:
        if i['lugar'] == "casa":
            hogar.append(object_answer("text", i['manera']))
    return array_answer(hogar, "lo que diga Andrr")


def prevencionTrabajo():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo = []
    for i in data:
        if i['lugar'] == "trabajo":
            trabajo.append(object_answer("text", i['manera']))
    return array_answer(trabajo, "lo que diga Andrr")


def chProvincia():
    data = get_data("centrosHabilitados", "centrosHabilitados")
    ch = []
    for i in data:
        ch.append(object_answer("text", i['provincia']))
    return array_answer(ch, "lo que diga Andrr")


def chCiudad():
    data = get_data("centrosHabilitados", "centrosHabilitados")
    ch = []
    for i in data:
        ch.append(object_answer("text", i['ciudad']))
    return array_answer(ch, "lo que diga Andrr")


def sintomas():
    data = get_data("sintomas", "sintomas")
    sintomas = []
    for i in data:
        sintomas.append(object_answer("text", i['nombre']))
    return array_answer(sintomas, "lo que diga Andrr")


def htEducacion():
    print("comando")
    return "oka"


def htTeletrabajo():
    print("comando")


def estadoCuarentena():
    print("comando")
    return "oka"


def mediosComunicacion():
    data = get_data("mediosComunicacion", "mediosComunicacion")
    sintomas = []
    for i in data:
        sintomas.append(object_answer("text", i['nombre']))
    return array_answer(sintomas, "lo que diga Andrr")


def ultimasNoticias():
    data = get_data("noticias", "noticias")
    ultima = data[-1]
    return array_answer((object_data_noticia("text", ultima['titulo'], ultima['resumen'], ultima['fuente'], ultima['fecha'])), "lo que diga Andrr")


def commands(argument):
    func = switcher.get(argument, lambda: {"error": "Invalid command"})
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
