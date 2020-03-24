from .commands_functions import *
from flask import jsonify
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
