#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Bot for Kamila Zolotova - Psychologist
Quiz: "Test for burnout/emotional state"
Works 24/7 on server
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('/var/log/telegram_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot token
BOT_TOKEN = "8467045900:AAH_GiX9XROEnReldI8-htApe2-7B8NzpcA"

# Store user data
user_data = {}

# Questions
QUESTIONS = [
    {
        "text": "❓ Вопрос 1 из 5\n\nКак вы обычно чувствуете себя утром, просыпаясь на работу?",
        "options": [
            ("🌅 С бодростью", 1),
            ("😴 Утро тяжело, но потом норм", 2),
            ("😰 С тревогой", 3),
            ("💤 Хочется спать ещё", 4)
        ]
    },
    {
        "text": "❓ Вопрос 2 из 5\n\nЧто происходит с энергией в течение дня?",
        "options": [
            ("⚡ Хватает до вечера", 1),
            ("📉 К обеду усталость", 2),
            ("🔋 Утром есть силы, к вечеру нет", 3),
            ("🪫 Разбит всё время", 4)
        ]
    },
    {
        "text": "❓ Вопрос 3 из 5\n\nКак часто думаете о работе вне рабочего времени?",
        "options": [
            ("🌟 Редко — отключаюсь", 1),
            ("📱 Иногда проверяю сообщения", 2),
            ("🔄 Часто кручу задачи", 3),
            ("😵 Постоянно, даже ночью", 4)
        ]
    },
    {
        "text": "❓ Вопрос 4 из 5\n\nЕсть физические симптомы: головные боли, боли в спине, нарушения сна?",
        "options": [
            ("✅ Нет, всё хорошо", 1),
            ("⚠️ Иногда", 2),
            ("🤕 Да, регулярно", 3),
            ("😷 Постоянно", 4)
        ]
    },
    {
        "text": "❓ Вопрос 5 из 5\n\nЧто чувствуете, думая о работе?",
        "options": [
            ("❤️ Удовлетворение", 1),
            ("😐 Нейтрально", 2),
            ("😤 Раздражение", 3),
            ("🚫 Хочу бросить", 4)
        ]
    }
]

def get_result(score):
    """Get result based on score"""
    if score <= 8:
        return {
            "emoji": "🟢",
            "title": "Хорошие новости!",
            "text": """Ваше состояние стабильное. Вы умеете восстанавливаться и держать баланс.

💡 Рекомендация: Продолжайте практики, которые работают.

📚 Материалы: https://pozitiv-psychology.ru/resources.html

Записаться на консультацию: @Kamila_Zolotova"""
        }
    elif score <= 13:
        return {
            "emoji": "🟡",
            "title": "Внимание — сигнал тревоги.",
            "text": """Организм подает признаки перегрузки. Это поправимо, если действовать сейчас.

💡 Рекомендации:
• Введите границы между работой и отдыхом
• Практикуйте дыхание
• Не игнорируйте симптомы

🆘 Я помогаю вернуться к норме до серьёзного выгорания.

Записаться: @Kamila_Zolotova"""
        }
    else:
        return {
            "emoji": "🔴",
            "title": "Важно действовать.",
            "text": """Признаки эмоционального выгорания. Это не ваша вина — следствие перегрузки.

⚠️ Не откладывайте:
• Обратитесь за помощью
• Дайте себе отдых
• Поговорите со специалистом

🆘 Я работаю с такими состояниями каждый день.

Запишитесь сейчас: @Kamila_Zolotova"""
        }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message"""
    keyboard = [
        [InlineKeyboardButton("📝 Пройти тест", callback_data='quiz_start')],
        [InlineKeyboardButton("📚 Полезные статьи", callback_data='articles')],
        [InlineKeyboardButton("💬 Записаться", callback_data='consultation')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        """👋 Здравствуйте! Я помогаю Камиле Золотовой — психологу КПТ.

За 3 минуты тест поможет понять состояние вашей нервной системы.

⚠️ Это не диагностика, а способ прислушаться к себе.

Чем помочь? 👇""",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button presses"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    user_id = query.from_user.id
    
    # Handle main menu buttons
    if data == 'articles':
        await query.edit_message_text(
            """📚 Полезные материалы:

• Когда работа с тревогой превращается в выгорание
• Почему умные люди попадаются на мошенников  
• Как справляться с тревожностью

https://pozitiv-psychology.ru/resources.html

Назад: /start"""
        )
        return
    
    if data == 'consultation':
        await query.edit_message_text(
            """💬 Запись на консультацию

Камила работает с:
• Выгоранием
• Тревожностью
• Последствиями мошенничества

👉 @Kamila_Zolotova

Назад: /start"""
        )
        return
    
    # Handle quiz start
    if data == 'quiz_start':
        user_data[user_id] = {'score': 0, 'question': 0}
        await ask_question(query, 0)
        return
    
    # Handle quiz answers
    if data.startswith('answer_'):
        parts = data.split('_')
        q_num = int(parts[1])
        score = int(parts[2])
        
        # Add score
        if user_id in user_data:
            user_data[user_id]['score'] += score
            user_data[user_id]['question'] = q_num + 1
        
        # Next question or result
        next_q = q_num + 1
        if next_q < len(QUESTIONS):
            await ask_question(query, next_q)
        else:
            await show_result(query, user_id)
        return
    
    # Handle restart
    if data == 'quiz_restart':
        user_data[user_id] = {'score': 0, 'question': 0}
        await ask_question(query, 0)
        return

async def ask_question(query, q_num):
    """Ask a question"""
    question = QUESTIONS[q_num]
    
    keyboard = []
    for option_text, score in question["options"]:
        callback = f'answer_{q_num}_{score}'
        keyboard.append([InlineKeyboardButton(option_text, callback_data=callback)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await query.edit_message_text(
            question["text"],
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error in ask_question: {e}")
        await query.message.reply_text(
            question["text"],
            reply_markup=reply_markup
        )

async def show_result(query, user_id):
    """Show quiz result"""
    score = user_data.get(user_id, {}).get('score', 10)
    result = get_result(score)
    
    keyboard = [
        [InlineKeyboardButton("💬 Записаться", url="https://t.me/Kamila_Zolotova")],
        [InlineKeyboardButton("📝 Пройти снова", callback_data='quiz_restart')],
        [InlineKeyboardButton("📚 Статьи", callback_data='articles')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"""{result['emoji']} {result['title']}

{result['text']}"""
    
    try:
        await query.edit_message_text(message, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in show_result: {e}")
        await query.message.reply_text(message, reply_markup=reply_markup)
    
    # Clean up
    if user_id in user_data:
        del user_data[user_id]
    
    logger.info(f"User {user_id} completed quiz with score {score}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Произошла ошибка. Напишите /start чтобы начать заново."
        )

def main():
    """Start the bot"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_error_handler(error_handler)
    
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()