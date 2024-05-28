import requests
import logging  # модуль для сбора логов
# подтягиваем константы из config файла
from config import LOGS, MAX_GPT_TOKENS, SYSTEM_PROMPT, IAM_TOKEN, FOLDER_ID

# настраиваем запись логов в файл
logging.basicConfig(filename=LOGS, level=logging.ERROR,
                    format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="w")


# подсчитываем количество токенов в сообщениях
def count_gpt_tokens(messages):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'modelUri': f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "messages": messages
    }
    try:
        response = requests.post(url=url, json=data, headers=headers)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        response_data = response.json()

        # Проверка наличия ключа 'tokens'
        if 'tokens' not in response_data:
            logging.error(f"Ошибка GPT. Ответ не содержит 'tokens': {response_data}")
            return 0

        return len(response_data['tokens'])

    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка HTTP запроса: {e}")
        return 0
    except (KeyError, ValueError) as e:
        logging.error(f"Ошибка обработки ответа: {e}")
        return 0
    except Exception as e:
        logging.error(f"Непредвиденная ошибка GPT: {e}")
        return 0

# запрос к GPT
def ask_gpt(messages):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'modelUri': f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": MAX_GPT_TOKENS
        },
        "messages": SYSTEM_PROMPT + messages  # добавляем к системному сообщению предыдущие сообщения
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        # проверяем статус код
        if response.status_code != 200:
            return False, f"Ошибка GPT. Статус-код: {response.status_code}", None
        # если всё успешно - считаем количество токенов, потраченных на ответ, возвращаем статус, ответ, и количество
        # токенов в ответе
        answer = response.json()['result']['alternatives'][0]['message']['text']
        tokens_in_answer = count_gpt_tokens([{'role': 'assistant', 'text': answer}])
        return True, answer, tokens_in_answer
    except Exception as e:
        logging.error(e)  # если ошибка - записываем её в логи
        return False, "Ошибка при обращении к GPT", None
