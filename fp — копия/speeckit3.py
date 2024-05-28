import requests
from config import IAM_TOKEN, FOLDER_ID

def speech_to_text(data):
    # Указываем параметры запроса
    params = "&".join([
        "topic=general",  # используем основную версию модели
        f"folderId={FOLDER_ID}",
        "lang=ru-RU"  # распознаём голосовое сообщение на русском языке
    ])

    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }

    # Выполняем запрос
    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    # Читаем json в словарь
    decoded_data = response.json()
    # Проверяем, не произошла ли ошибка при запросе
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")  # Возвращаем статус и текст из аудио
    else:
        return False, "При запросе в SpeechKit возникла ошибка"


def text_to_speech(text):

    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}"
    }
    data = {
        "text": text,
        "lang": "ru-RU",
        "voice": "alyss",
        "folderId": FOLDER_ID
    }
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"
