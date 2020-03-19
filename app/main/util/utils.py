def getList(dict):
    return dict.keys()


def object_data(answer_type, answer, description):
    """
     {"answer":[{"answer_type":"text", "answer":" "Usar gel antibacterial en la manos""}], "description":"Estas con las maneras de prevenirse en el transpore"}
    """
    return {
        "answer": [{"answer_type": answer_type, "answer": answer, "description": description}]
    }
