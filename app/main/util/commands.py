
def prevencionTransporte():
    print("comando")
    return "oka"
def prevencionHogar():
    print("comando")
    return "oka"
def prevencionTrabajo():
    print("comando")
    return "oka"
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
    switcher ={
    "PrevencionTransporte":prevencionTransporte,
    "PrevencionHogar":prevencionHogar,
    "PrevencionTrabajo":prevencionTrabajo,
    "CHProvincia":chProvincia,
    "CHCiudad":chCiudad,
    "sintomas":sintomas,
    "HTEducacion":htEducacion,
    "HTTeletrabajo":htTeletrabajo,
    "estadoCuarentena":estadoCuarentena,
    "MediosComunicacion":mediosComunicacion,
    "UltimasNoticias":ultimasNoticias,
    }
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func()
