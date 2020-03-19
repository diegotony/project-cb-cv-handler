def getList(dict):
    return dict.keys()


def object_answer(answer_type, answer):
    return {"answer_type": answer_type, "answer": answer}


def object_data_noticia(answer_type, answer,resumen,fuente,fecha):
    return {"answer_type": answer_type, "answer": answer,"resumen":resumen,"fuente":fuente,"fecha":fecha}

def array_answer(array_answers, description):
    return {
        "answer": array_answers, "description": description
    }


def messsage(status, accion, id):
    return {"status": status, "message": accion, "id": id}


def messsage_error(status, accion):
    return {"status": status, "message": accion}

def array_interaccions(data):
    array_data=[]
    for i in data:
        array_data.append(
            {"user_id":i.user_id,
            "input_db":i.input_db,
            "output_db": i.output_db,
            })
    # print(array_data)
    return {"data":array_data}