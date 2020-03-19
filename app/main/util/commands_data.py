commands_list = [
    {"comando": "Prevencion", "description": "Enterate de las medidas de prevencion en diferentes medios",
        "parent": True, "child": ["Transporte", "Hogar", "Trabajo"]},
    {"comando": "ComoColaborar", "answer": "Puedes colaborar escribiendonos a INFORMACION PENDIENTE",
     "description": "Contacta con nostros!", "parent": True},
    {"comando": "Prevencion", "description": "Enterate de las medidas de prevencion en diferentes medios",
     "parent": True,
     "child": ["Transporte", "Hogar", "Trabajo"]},
    {"comando": "Transporte", "description": "Medidas de movilización", "parent": False},
    {"comando": "Hogar", "description": "Medidas de prevencion en el hogar", "parent": False},
    {"comando": "Trabajo",
        "description": "Medidas de prevencion para tu trabajo", "parent": False},
    {"comando": "CentrosHabilitados", "description": "Conoce los centros habilitados en el pais", "parent": True,
     "child": ["PorProvincia", "PorCiudad"]},
    {"comando": "PorProvincia",
        "description": "Centros médicos disponibles", "parent": False},
    {"comando": "PorCiudad", "description": "Centros médicos disponibles ", "parent": False},
    {"comando": "Sintomas", "description": "Sintomas relacionado al cuadro de una persona con covid-19",
     "parent": True},
    {"comando": "HerramientasTeletrabajo", "description": "Herramientas que te pueden interesar", "parent": True,
     "child": ["Educacion", "Teletrabajo"]},
    {"comando": "Educacion",
        "description": "Herramientas para profesores y estudiantes", "parent": False},
    {"comando": "Teletrabajo",
        "description": "Herramientas para el trabajo desde casa", "parent": False},
    {"comando": "EstadoCuarentena",
        "description": "Ultimas noticias de la cuarentena", "parent": False},
    {"comando": "MediosComunicacion",
        "description": "Medios oficiales para informarte", "parent": False},
    {"comando": "UltimasNoticias",
        "description": "Qué pasa con el covid-19 a nivel mundial", "parent": False},
    {"comando": "ReportarCaso",
        "description": "Cónoces algún caso? Reportalo", "parent": True},
    {"comando": "ComoColaborar", "answer": "Puedes colaborar escribiendonos a (INFORMACION PENDIENTE)",
     "description": "Contacta con nostros!", "parent": True},

]