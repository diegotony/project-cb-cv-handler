def getList(dict):
    return dict.keys()


def object_data(answer_type, answer):
    return {"answer_type": answer_type, "answer": answer}


def object_data_noticia(answer_type, answer,resumen,fuente,fecha):
    return {"answer_type": answer_type, "answer": answer,"resumen":resumen,"fuente":fuente,"fecha":fecha}

def array_data(array_answers, description):
    return {
        "answer": array_answers, "description": description
    }
