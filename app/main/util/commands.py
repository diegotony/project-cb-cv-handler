from flask import jsonify
import random
from .commands_data import commands_list
from .api_requets import get_data
from .utils import object_answer, array_answer, object_data_noticia, check_type


def prevencionTransporte():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    transporte = []
    for i in data:
        if i['lugar'] == "transporte":
            if check_type(i['manera']) == "text":
                transporte.append(object_answer("text", i['manera']))
    return array_answer(transporte, "Estas son las medidas de prevencion en el transporte:")


def prevencionHogar():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    hogar=[]
    for i in data:
        if i['lugar'] == "casa":
            if check_type(i['manera']) == "text":
                hogar.append(object_answer(check_type(i['manera']), i['manera']))

    list_five =random.sample(hogar,5)

    return array_answer(list_five, "Estas son las medidas de prevencion en el trabajo:")


def prevencionTrabajo():
    data = get_data("manerasPrevencion", "manerasPrevencion")
    trabajo = []
    for i in data:
        if i['lugar'] == "trabajo":
            if check_type(i['manera']) == "text":
                trabajo.append(object_answer("text", i['manera']))
    return array_answer(trabajo, "Estas son las medidas de prevencion en el hogar:")


def chProvincia():
    data = get_data("centrosHabilitados", "centrosHabilitados")
    ch = []
    for i in data:
        ch.append(object_answer("text", i['hospital']+"({0})".format(i['provincia'])))
    return array_answer(ch, "Estos son los centros habilitados en las diferentes provincias del Ecuador")


def chCiudad():
    data = get_data("centrosHabilitados", "centrosHabilitados")
    ch = []
    for i in data:
        if check_type(i['ciudad']) == "text":
            ch.append(object_answer("text", i['hospital']+"({0})".format(i['ciudad'])))
    return array_answer(ch, "Estos son los centros habilitados en las diferentes ciudades del Ecuador")


def sintomas():
    data = get_data("sintomas", "sintomas")
    sintomas = []
    for i in data:
        if check_type(i['nombre']) == "text":
            sintomas.append(object_answer(check_type(i['nombre']), i['nombre']))

    return array_answer(sintomas, "No tiene")


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
    medios = []
    print(data)
    for i in data:
        medios.append(object_answer("text", i['nombre'] + " ({0})".format(i['redes']['web'])))
    return array_answer(medios, "Informate de Medios de Comunicacion oficiales:")


def ultimasNoticias():
    data = get_data("noticias", "noticias")
    ultimas = []
    # for i in data:
    #     ultimas.append(object_answer("text","{0} ({1})".format(i['titulo'],i['fuente'])))
    ultimas.append(object_answer("text","{0} ({1})".format(data[-1]['titulo'],data[-1]['fuente'])))
    ultimas.append(object_answer("text","{0} ({1})".format(data[-2]['titulo'],data[-1]['fuente'])))
    ultimas.append(object_answer("text","{0} ({1})".format(data[-3]['titulo'],data[-1]['fuente'])))
    ultimas.append(object_answer("text","{0} ({1})".format(data[-4]['titulo'],data[-1]['fuente'])))
    ultimas.append(object_answer("text","{0} ({1})".format(data[-5]['titulo'],data[-1]['fuente'])))

    return array_answer(ultimas,"Ultimas noticias del covid-19 en el Ecuador")

def reportarCaso():
    pass


def commands(argument):
    func = switcher.get(argument, lambda: {"error": "Invalid command"})
    return func()


def get_all_commands():
    print(commands)
    return jsonify(commands_list)


switcher = {
    "transporte": prevencionTransporte,
    "hogar": prevencionHogar,
    "trabajo": prevencionTrabajo,
    "porprovincia": chProvincia,
    "porciudad": chCiudad,
    "sintomas": sintomas,
    "educacion": htEducacion,
    "teletrabajo": htTeletrabajo,
    "estadoCuarentena": estadoCuarentena,
    "medios": mediosComunicacion,
    "ultimasnoticias": ultimasNoticias,
    "reportar":reportarCaso,
}
