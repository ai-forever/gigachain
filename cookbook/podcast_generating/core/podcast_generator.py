"""
Упрощенный генератор диалоговых подкастов
"""

import os
from typing import Optional, Dict, Any
from langchain.llms import GigaChat
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.manager import CallbackManager
import json
import re
import requests
import time



# Универсальный промпт для диалогового подкаста
UNIVERSAL_DIALOGUE_PROMPT = """
Ты - сценарист популярного диалогового подкаста. Создай увлекательный сценарий для двух ведущих: Алиса (интервьюер, девушка) и Михаил (эксперт, мужчина).

ТЕКСТ:
{text}

ТРЕБОВАНИЯ:
- Длительность: {duration} минут
- Формат: естественный диалог между интервьюером и экспертом
- Алиса задает интересные вопросы, Михаил дает экспертные ответы
- Каждая реплика на отдельной строке с указанием говорящего
- Разговорный стиль, избегать сухого академического языка
- Включить элементы вовлечения, юмора и практических примеров

СТРУКТУРА:
1. Вступление и знакомство (1-2 минуты)
2. Основная часть - обсуждение темы (основное время)
3. Заключение и прощание (1-2 минуты)

ФОРМАТ ВЫВОДА:
Алиса: [реплика Алисы]
Михаил: [ответ Михаила]
Алиса: [следующая реплика]
Михаил: [ответ]
...

Стиль Алисы: любознательная, дружелюбная, иногда задает провокационные вопросы, представляет точку зрения обычного человека
Стиль Михаила: эксперт, спокойный, с юмором, дает практические советы, объясняет сложное простым языком
"""


class TokenUsageCallback(BaseCallbackHandler):
    """Callback для отслеживания использования токенов"""
    
    def __init__(self):
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        self.requests_count = 0
        self.last_response = None
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: list, **kwargs):
        """Вызывается при начале генерации"""
        self.requests_count += 1
    
    def on_llm_end(self, response, **kwargs):
        """Вызывается при завершении генерации"""
        self.last_response = response
        token_info = response.llm_output["token_usage"]
        self.token_usage["prompt_tokens"] += token_info.prompt_tokens
        self.token_usage["completion_tokens"] += token_info.completion_tokens
        self.token_usage["total_tokens"] += token_info.total_tokens


class PodcastGenerator:
    def __init__(self, username: str, password: str, GIGACHAT_URL: str):
        """
        Инициализация упрощенного генератора подкастов
        
        Args:
            username: Логин для GigaChat
            password: Пароль для GigaChat
            GIGACHAT_URL: URL для GigaChat API
        """
        # Создаем callback для отслеживания токенов
        self.token_callback = TokenUsageCallback()
        self.callback_manager = CallbackManager([self.token_callback])
        
        self.llm = GigaChat(
            user=username,
            password=password,
            base_url=GIGACHAT_URL+"/v1",
            auth_url=GIGACHAT_URL+"/v1/token",
            model="GigaChat-2-Max",
            temperature=0.1,
            scope="GIGACHAT_API_CORP",
            verify_ssl_certs=False,
            timeout=180000,
            callbacks=[self.token_callback],
            verbose=False,  # Включаем verbose для лучшего отслеживания
            use_api_for_tokens=True,
        )
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=3000,
            chunk_overlap=200,
            length_function=len,
        )
    
    def generate_podcast(self, text: str, duration: Optional[int] = None) -> str:
        """
        Генерирует диалоговый подкаст на основе текста
        
        Args:
            text: Исходный текст
            duration: Длительность подкаста в минутах (если None, рассчитывается автоматически)
        
        Returns:
            Сгенерированный диалоговый сценарий
        """
        # Автоматический расчет длительности, если не указана
        if duration is None:
            duration = self.calculate_optimal_duration(len(text))
        
        # Если текст слишком длинный, разбиваем его на части
        if len(text) > 3000:
            chunks = self.text_splitter.split_text(text)
            text = " ".join(chunks[:3])
        
        # Форматируем промпт напрямую
        formatted_prompt = UNIVERSAL_DIALOGUE_PROMPT.format(text=text, duration=duration)
        
        # Вызываем LLM напрямую
        result = self.llm.invoke(formatted_prompt)
        
        return result
    
    def reset_token_usage(self):
        """Сбрасывает счетчики токенов"""
        self.token_callback.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        self.token_callback.requests_count = 0
    
    def estimate_tokens_for_text(self, text: str) -> Dict[str, int]:
        """
        Оценивает количество токенов для текста
        
        Args:
            text: Текст для оценки
        
        Returns:
            Словарь с оценкой токенов
        """
        # Простая оценка: примерно 1 токен = 4 символа для русского текста
        # Более точная оценка требует токенизатора
        estimated_tokens = len(text) // 4
        
        return {
            "estimated_tokens": estimated_tokens,
            "text_length": len(text),
            "word_count": len(text.split())
        }
    
    def calculate_optimal_duration(self, text_length: int) -> int:
        """
        Рассчитывает оптимальную длительность подкаста на основе размера текста
        
        Args:
            text_length: Длина текста в символах
        
        Returns:
            Рекомендуемая длительность в минутах
        """
        # Примерная формула: 1 минута = 150-200 слов = 1000-1500 символов
        if text_length < 5000:
            return 5
        elif text_length < 10000:
            return 8
        elif text_length < 20000:
            return 12
        elif text_length < 35000:
            return 15
        else:
            return 20
