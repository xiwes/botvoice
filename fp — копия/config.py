TOKEN = '7088477361:AAF5zj6iIghuqk1UnQJjC2VTpurMbXZBB9E'  # token телеграм-бота

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

IAM_TOKEN = ('t1.9euelZqTis2QlZmVmM3Jz5uQy8aYi-3rnpWaycbPipjHnJTJl5jLkomanM_l8_dMRzNN-e83eTIj_t3z9wx2ME357zd5MiP-zef1656Vms6Jnsydy8zOnZKNjc6Vkc2e7_zF656Vms6Jnsydy8zOnZKNjc6Vkc2eveuelZqXnsbKyIyNnpPLkMqNxpyNibXehpzRnJCSj4qLmtGL'
'mdKckJKPioua0pKai56bnoue0oye.qAdCnH2hBkO7qrmu_P7RPgaxscOTlMuftShS5hFyODZIxbPzOZGbGkopl6ZRIC1Ih2v3wWxvpuYd3nEANwuMDw')
FOLDER_ID = 'b1gnbppcbqh85bmnuiqf'
# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

LOGS = 'logs.txt'  # файл для логов
DB_FILE = 'messages.sql'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом
