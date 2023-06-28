import uuid


def gerar_id():
    uid = uuid.uuid4()
    id_pequeno = str(uid).replace("-", "")[:5]
    return id_pequeno
