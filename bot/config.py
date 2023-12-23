import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("6609962299:AAFjKbnHk4ZLOgIGQl7b77xXztMGmUPMOLc", None)
    PYRO_SESSION = getenv("BAF39SsAh1NI60jY7oJqaHK7bnSB9n_UyWUifw7qvRaf_tbPqVVL64geaNOYfmnNz_nUxo1c9OOgsy9Sl11kAdydt2uUkyUNxLdlMlc9xioi7i9YObgoX-b8OxugDpzJaydZ9MGdB-qf7qk5gHddpIZc4vLeLS0NplPR2U65fIzyhCm9oHJvi75fH7AClwIVLaZr7TLQ_kk071HULWQEC0KHHkiodSoD_0DmadE0jR8aPMqgvtRmB-CJLEuc5EX9aqb7q-QnkaPsF0IhPVSKPz7j4uYgdJAxD3pAitx6n4_qAv-ho4DLwnmLkTzh119O4FYzcrTRQAduCaP6Jd8NyNXs2H_d3QAAAAFTuY5kAA", None)
    TELEGRAM_APP_HASH= getenv('e02a72843ababb75de3c4f3aa2ce8d75')
    TELEGRAM_APP_ID=int(getenv('24638763'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
