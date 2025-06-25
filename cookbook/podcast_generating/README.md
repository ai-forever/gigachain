# 🎙️ AI-Powered Podcast Generator Workshop

**Автоматизированная система генерации диалоговых подкастов с использованием искусственного интеллекта**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)](https://langchain.com/)
[![GigaChat](https://img.shields.io/badge/GigaChat-API-orange.svg)](https://developers.sber.ru/portal/products/gigachat)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Обзор проекта

Этот проект демонстрирует современные подходы к автоматизации создания контента с использованием AI. Система генерирует диалоговые подкасты на основе текстовых документов, используя:

- **GigaChat API** для генерации контента
- **LangChain** для работы с языковыми моделями
- **PDF обработку** для извлечения текста
- **TTS оптимизацию** для подготовки к озвучиванию
- **Отслеживание токенов** для контроля расходов

## ✨ Ключевые возможности

### 🎯 Основной функционал
- **Диалоговые подкасты** с двумя персонажами (Алиса + Михаил)
- **Автоматический расчет длительности** на основе объема контента
- **Извлечение текста** из PDF документов и веб-страниц
- **Отслеживание токенов** GigaChat для контроля расходов

### 🔧 Технические особенности
- **Модульная архитектура** с разделением на core компоненты
- **Jupyter Notebook** для интерактивной работы
- **Docker контейнеризация** для простоты воспроизведения
- **Два способа отслеживания токенов**: через LangChain callbacks и прямые API вызовы

## 🛠️ Технологический стек

| Компонент | Технология | Назначение |
|-----------|------------|------------|
| **AI/ML** | GigaChat API | Генерация контента |
| **Framework** | LangChain | Работа с LLM |
| **Document Processing** | PyPDF, pdfplumber | Обработка PDF |
| **Web Scraping** | BeautifulSoup, WeasyPrint | Скачивание веб-страниц |
| **Audio Processing** | pydub | Обработка аудио |
| **Token Tracking** | Custom Callbacks | Отслеживание токенов |
| **Development** | Jupyter, Python | Разработка и тестирование |
| **Deployment** | Docker | Контейнеризация |

## 📦 Установка и настройка

### Предварительные требования
```bash
# Python 3.8+
python --version

# Git
git --version

# Docker (опционально)
docker --version
```

### Быстрая установка
```bash
# Клонирование репозитория
git clone <repository-url>
cd podcasting_workshop

# Создание виртуального окружения
python -m venv env
source env/bin/activate  # Linux/Mac
# или
env\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt
```

### Настройка API ключей
```bash
# Настройка переменных окружения
export GIGACHAT_USERNAME="your_username"
export GIGACHAT_PASSWORD="your_password"
export GIGACHAT_URL="https://gigachat.devices.sberbank.ru"
export SALUTESPEECH_AUTH_TOKEN="token"
```

## 🎮 Использование

### Базовый пример
```python
from core.podcast_generator import PodcastGenerator
from core.pdf_text_extractor import extract_text

# Инициализация генератора
generator = PodcastGenerator(
    username="your_username",
    password="your_password", 
    GIGACHAT_URL="gigachat_url"
)

# Извлечение текста из PDF
text = extract_text("document.pdf")

# Генерация диалогового подкаста
script = generator.generate_podcast(text, duration=10)
print(script)

### Интерактивная работа через Jupyter
```bash
# Запуск Jupyter Notebook
jupyter notebook workshop.ipynb
```

## 🐳 Docker развертывание

```bash
# Сборка образа
docker build -f docker/Dockerfile -t podcast-generator .

# Запуск контейнера
docker run -p 8888:8888 -e GIGACHAT_USERNAME=user -e GIGACHAT_PASSWORD=pass podcast-generator -e SALUTESPEECH_AUTH_TOKEN=token 
```


---

**⭐ Если проект оказался полезным, поставьте звездочку!**