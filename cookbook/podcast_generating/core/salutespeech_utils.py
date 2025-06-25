"""
salutespeech_utils.py

Модуль для работы с Sber SmartSpeech TTS API
"""

import os
import uuid
import time
import httpx
import aiofiles
import requests
import logging
from loguru import logger
from typing import Optional, Any


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Константы для Sber TTS
SBER_AUTH_TOKEN = os.environ["SALUTESPEECH_AUTH_TOKEN"]
SBER_TTS_RETRY_ATTEMPTS = 3
SBER_TTS_RETRY_DELAY = 5

# Глобальная переменная для токена доступа
_salute_access_token = None


def get_sber_tts_token_sync(auth_token: str, scope: str = 'SALUTE_SPEECH_CORP') -> Optional[str]:
    """Получение токена доступа для Sber SmartSpeech API."""
    if not auth_token:
        logger.error("SALUTE_SPEECH токен не установлен в переменных окружения")
        return None
        
    rq_uid = str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }
    payload = {'scope': scope}
    
    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response.raise_for_status()
        token = response.json()['access_token']
        logger.info("Токен Sber TTS успешно получен")
        return token
    except requests.RequestException as e:
        logger.error(f"Ошибка получения токена Sber TTS: {str(e)}")
        if 'response' in locals():
            logger.error(f"Ответ сервера: {response.text}")
        return None
    except KeyError:
        logger.error(f"Ошибка: 'access_token' не найден в ответе. Ответ: {response.text}")
        return None


def synthesize_sber_speech_sync(
    text: str, 
    output_filename: str, 
    format: str = 'wav16', 
    voice: str = 'Bys_24000',
    mood: Any = None
) -> bool:
    """Синтез речи через Sber SmartSpeech API."""
    global _salute_access_token
    if mood:
        assert mood in ['whisper', 'sad', 'annoyed', 'happy']
        text = f'<speak><voice mode="{mood}">{text}</voice></speak>'

    # Получаем токен при первом вызове
    if _salute_access_token is None:
        _salute_access_token = get_sber_tts_token_sync(SBER_AUTH_TOKEN)
        if _salute_access_token is None:
            return False
    
    url = "https://smartspeech.sber.ru/rest/v1/text:synthesize"
    headers = {
        "Authorization": f"Bearer {_salute_access_token}",
        "Content-Type": "application/ssml" if mood else "application/text"
    }
    params = {
        "format": format, 
        "voice": voice,
    }
    
    for attempt in range(SBER_TTS_RETRY_ATTEMPTS):
        try:
            response = requests.post(
                url, 
                headers=headers, 
                params=params, 
                # data=text.encode('utf-8'), 
                data=text, 
                verify=False
            )
            response.raise_for_status()
            
            with open(output_filename, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"Аудио синтезировано: {output_filename}")
            return True
            
        except requests.RequestException as e:
            logger.error(f"Ошибка синтеза речи (попытка {attempt + 1}): {str(e)}")
            if 'response' in locals():
                logger.error(f"Ответ сервера: {response.text}")
            
            if attempt == SBER_TTS_RETRY_ATTEMPTS - 1:
                return False
            
            time.sleep(SBER_TTS_RETRY_DELAY)
    
    return False
