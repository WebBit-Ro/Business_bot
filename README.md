# 🤖 Telegram Business Card & FAQ Bot

**🌐 Language / Мова / Язык:** [🇬🇧 English](#-english) · [🇺🇦 Українська](#-українська) · [🇷🇺 Русский](#-русский)

---

## 🇬🇧 English

A lightweight, modular Telegram bot built with **Python 3.11+** and **aiogram 3.x** that acts as an interactive digital business card and first-line customer support assistant.

Designed for service businesses, studios, and freelancers to present services, answer common questions, share working hours, and route warm leads directly to a manager.

### ✨ Key Features

- **Interactive Inline Navigation:** Clean, single-message menu structure (`edit_text`) that keeps the chat clutter-free without spamming message history.
- **Core Business Sections:**
  - **Services & Pricing:** Structured overview of available packages and rates.
  - **Working Hours & Location:** Clear schedule, address, and service area details.
  - **Interactive FAQ:** Instant answers to common client questions with one-tap return to the main menu.
  - **Manager Handoff / Lead Capture:** Direct connection to a manager or step-by-step lead collection with admin notifications.
- **Input Validation & Safety:** Built-in regex validation for phone numbers and Telegram usernames, HTML escaping for user inputs, and graceful Telegram API error handling.
- **Zero-Database Footprint:** Uses `aiogram` FSM (`MemoryStorage`) for lightweight, fast deployment without external database overhead.

### 🛠 Tech Stack

- **Language:** Python 3.11+
- **Framework:** [aiogram 3.x](https://aiogram.dev) (Asynchronous Telegram Bot API)
- **Configuration:** `python-dotenv` for environment variable management
- **Architecture:** Router-based modular handlers & Finite State Machine (FSM)

### 📂 Project Structure

```text
telegram_business_card_bot/
├── main.py              # Bot entry point, routers, keyboards, and FSM handlers
├── config.py            # Environment variables loader and validation
├── requirements.txt     # Project dependencies
├── .env.example         # Template for required environment variables
└── README.md            # Project documentation
```

### 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd telegram-business-card-bot
   ```

2. **Create a virtual environment & install dependencies:**
   *Windows (PowerShell):*
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
   *macOS / Linux:*
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Copy `.env.example` to `.env` and fill in your credentials:
   ```env
   BOT_TOKEN=your_telegram_bot_token_from_botfather
   ADMIN_CHAT_ID=123456789
   ```
   > **Note:** Start a chat with your bot (`/start`) from the admin account first so Telegram allows the bot to deliver notifications to `ADMIN_CHAT_ID`.

4. **Run the bot:**
   ```bash
   python main.py
   ```

🔼 [Back to top](#-telegram-business-card--faq-bot)

---

## 🇺🇦 Українська

Легкий модульний Telegram-бот на **Python 3.11+** та **aiogram 3.x**, який працює як інтерактивна цифрова візитівка та помічник першої лінії підтримки.

Створений для сфери послуг, студій і фрилансерів, щоб презентувати послуги, відповідати на часті запитання, показувати графік роботи та передавати заявки менеджеру.

### ✨ Основні можливості

- **Зручна інлайн-навігація:** усі розділи відкриваються в одному повідомленні (`edit_text`), не засмічуючи історію чату зайвими повідомленнями.
- **Ключові розділи для бізнесу:**
  - **Послуги та ціни (Services & Pricing):** структурований опис пакетів і тарифів.
  - **Графік роботи та локація (Working Hours & Location):** розклад, адреса та зона обслуговування.
  - **Інтерактивний FAQ:** миттєві відповіді на часті запитання клієнтів із поверненням у головне меню в один клік.
  - **Зв'язок із менеджером / збір заявок:** швидкий перехід до діалогу або покрокове оформлення заявки зі сповіщенням адміністратора.
- **Валідація та безпека:** перевірка номерів телефону та юзернеймів через регулярні вирази (regex), екранування HTML і коректна обробка помилок Telegram API.
- **Без зовнішніх баз даних:** стани діалогу працюють через `aiogram` FSM (`MemoryStorage`), що спрощує розгортання бота на будь-якому сервері.

### 🛠 Технологічний стек

- **Мова:** Python 3.11+
- **Фреймворк:** [aiogram 3.x](https://aiogram.dev) (асинхронна робота з Telegram Bot API)
- **Конфігурація:** `python-dotenv` для керування змінними оточення
- **Архітектура:** модульні роутери та машина станів (FSM)

### 📂 Структура проєкту

```text
telegram_business_card_bot/
├── main.py              # Точка входу, роутери, клавіатури та обробники FSM
├── config.py            # Завантаження та перевірка змінних оточення
├── requirements.txt     # Залежності проєкту
├── .env.example         # Шаблон файлу конфігурації
└── README.md            # Документація проєкту
```

### 🚀 Швидкий запуск

1. **Клонуйте репозиторій:**
   ```bash
   git clone https://github.com
   cd telegram-business-card-bot
   ```

2. **Створіть віртуальне оточення та встановіть залежності:**
   *Windows (PowerShell):*
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
   *macOS / Linux:*
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Налаштуйте змінні оточення:**
   Скопіюйте `.env.example` у `.env` та вкажіть свої дані:
   ```env
   BOT_TOKEN=ваш_токен_від_botfather
   ADMIN_CHAT_ID=123456789
   ```
   > **Важливо:** спочатку відкрийте бота в Telegram з акаунта адміністратора та натисніть `/start`, щоб бот мав право надсилати вам сповіщення.

4. **Запустіть бота:**
   ```bash
   python main.py
   ```

🔼 [Нагору](#-telegram-business-card--faq-bot)

---

## 🇷🇺 Русский

Лёгкий модульный Telegram-бот на **Python 3.11+** и **aiogram 3.x**, который работает как интерактивная цифровая визитка и помощник первой линии поддержки.

Создан для сферы услуг, студий и фрилансеров, чтобы презентовать услуги, отвечать на частые вопросы, показывать график работы и передавать заявки менеджеру.

### ✨ Основные возможности

- **Удобная инлайн-навигация:** все разделы открываются внутри одного сообщения (`edit_text`), не засоряя историю чата лишними уведомлениями.
- **Ключевые разделы для бизнеса:**
  - **Услуги и цены (Services & Pricing):** структурированный обзор пакетов и тарифов.
  - **График работы и локация (Working Hours & Location):** расписание, адрес и зона обслуживания.
  - **Интерактивный FAQ:** мгновенные ответы на частые вопросы клиентов с возвратом в главное меню в один клик.
  - **Связь с менеджером / сбор заявок:** быстрый переход к диалогу или пошаговое оформление заявки с уведомлением администратора.
- **Валидация и безопасность:** проверка номеров телефона и юзернеймов через регулярные выражения (regex), экранирование HTML и корректная обработка ошибок Telegram API.
- **Без внешних баз данных:** состояния диалога работают через `aiogram` FSM (`MemoryStorage`), что упрощает запуск бота на любом сервере.

### 🛠 Технологический стек

- **Язык:** Python 3.11+
- **Фреймворк:** [aiogram 3.x](https://aiogram.dev) (асинхронная работа с Telegram Bot API)
- **Конфигурация:** `python-dotenv` для управления переменными окружения
- **Архитектура:** модульные роутеры и машина состояний (FSM)

### 📂 Структура проекта

```text
telegram_business_card_bot/
├── main.py              # Точка входа, роутеры, клавиатуры и обработчики FSM
├── config.py            # Загрузка и проверка переменных окружения
├── requirements.txt     # Зависимости проекта
├── .env.example         # Шаблон файла конфигурации
└── README.md            # Документация проекта
```

### 🚀 Быстрый запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd telegram-business-card-bot
   ```

2. **Создайте виртуальное окружение и установите зависимости:**
   *Windows (PowerShell):*
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
   *macOS / Linux:*
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения:**
   Скопируйте `.env.example` в `.env` и укажите свои данные:
   ```env
   BOT_TOKEN=ваш_токен_от_botfather
   ADMIN_CHAT_ID=123456789
   ```
   > **Важно:** сначала откройте бота в Telegram с аккаунта администратора и нажмите `/start`, чтобы бот мог отправлять вам уведомления.

4. **Запустите бота:**
   ```bash
   python main.py
   ```

🔼 [Наверх](#-telegram-business-card--faq-bot)
