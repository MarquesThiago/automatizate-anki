import requests
from typing import Dict, List


def add_note(note: dict):
    url = "http://127.0.0.1:8765"
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": note
        }
    }
    response = requests.post(url, json=payload)
    return response.json()


def add_embed(
    url: str, name: str, fields: List[str]
) -> Dict[str, str]:

    return {
        "url": url,
        "filename": name,
        "fields": fields
    }

# Exemplo de uso
# deck_name = "Nome do seu baralho"
# front_text = "Pergunta?"
# back_text = "Resposta."
# image_path = "/caminho/para/a/sua/imagem.jpg"

# response = add_note_with_image(deck_name, front_text, back_text, image_path)
# print(response)
