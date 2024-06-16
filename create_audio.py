from google.cloud import texttospeech
from gtts import gTTS

LIST_JAPONES_SPEAKER = [
    "ja-JP-Wavenet-A",
    "ja-JP-Wavenet-B",
    "ja-JP-Wavenet-C",
    "ja-JP-Wavenet-D",
    "ja-JP-Standard-A",
    "ja-JP-Standard-B",
    "ja-JP-Standard-C",
    "ja-JP-Standard-D"
]


def generate_audio(
        text, output_file, language="ja-JP", name=LIST_JAPONES_SPEAKER[0]
):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language,
        name=name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)


def generate_audio_gtts(text, output_file, lang="ja"):
    tts = gTTS(text=text, lang=lang)  # 'ja' é o código para japonês
    tts.save(output_file)
