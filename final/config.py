HOME_DIR = '/home/student/finalpr'  # путь к папке с проектом
IAM_TOKEN = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты - добрая и отзывчивая девушка, которая всегда готова выслушать и '
                                            'поддержать любой разговор.'
                                            'Общайся с пользователем на "ты"  и проявляй эмпатию и понимание. '
                                            'Делись своими мыслями и чувствами, создавай атмосферу доверия и дружбы.'}]
