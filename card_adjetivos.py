from typing import List, Dict


def note_adjetivos(
    deck_name: str,
    front: str,
    typing_: str,
    back: str,
    complemento: str,
    use: str,
    traduction: str,
    kanji: str,
    model="Infromation",
    tags: List[str] = [],
    audio: List[Dict[str, str]] = [],
    video: List[Dict[str, str]] = [],
    image: List[Dict[str, str]] = []
):

    return {
        "deckName": deck_name,
        "modelName": model,
        "fields": {
            "Frente": front,
            "player": "",
            "Type": typing_,
            "Verso": back,
            "complemento": complemento,
            "Uso": use,
            "uso-player": "",
            "Uso-Traducao": traduction,
            "kanji": kanji
        },
        "tags": tags,
        "audio": audio,
        "video": video,
        "picture": image
    }
