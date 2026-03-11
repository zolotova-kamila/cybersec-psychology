#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Bot for Kamila Zolotova - Psychologist
Quiz: "Test for burnout/emotional state"
Works 24/7 on server
"""

import logging
import json
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler
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

# States for ConversationHandler
QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, RESULT = range(6)

# Store user scores
user_scores = {}

# Questions and answers
QUESTIONS = [
    {
        "text": "❓ Вопрос 1 из 5\n\nКак вы обычно чувствуете себя утром, просыпаясь на работу?",
        "options": [
            ("🌅 С бодростью и энтузиазмом", 1),
            ("😴 Утро — это тяжело, но потом входишь в ритм", 2),
            ("😰 С тревогой и желанием закрыть глаза", 3),
            ("💤 Хочется спать ещё, сколько бы ни спал", 4)
        ]
    },
    {
        "text": "❓ Вопрос 2 из 5\n\nЧто происходит с вашей энергией в течение дня?",
        "options": [
            ("⚡ Энергии хватает до вечера", 1),
            ("📉 К обеду уже чувствуешь усталость", 2),
            ("🔋 Утром есть силы, к вечеру — полное истощение", 3),
            ("🪫 Чувствую себя разбитым всё время", 4)
        ]
    },
    {
        "text": "❓ Вопрос 3 из 5\n\nКак часто вы думаете о работе вне рабочего времени?",
        "options": [
            ("🌟 Редко — умею отключаться", 1),
            ("📱 Иногда проверяю сообщения", 2),
            ("🔄 Часто кручу задачи в голове", 3),
            ("😵 Постоянно, даже ночью", 4)
        ]
    },
    {
        "text": "❓ Вопрос 4 из 5\n\nЕсть ли у вас физические симптомы: головные боли, боли в шее/спине, нарушения сна?",
        "options": [
            ("✅ Нет, чувствую себя хорошо", 1),
            ("⚠️ Иногда, но не критично", 2),
            ("🤕 Да, бывает регулярно", 3),
            ("😷 Постоянно, мешают жить", 4)
        ]
    },
    {
        "text": "❓ Вопрос 5 из 5\n\nЧто вы чувствуете, думая о своей работе?",
        "options": [
            ("❤️ Удовлетворение и интерес", 1),
            ("😐 Это работа, нейтрально", 2),
            ("😤 Раздражение и усталость", 3),
            ("🚫 Хочу всё бросить", 4)
        ]
    }
]

# Results based on score
def get_result(score):
    if score <= 8:
        return {
            "emoji": "🟢",
            "title": "Хорошие новости!",
            "text": """Ваше состояние стабильное. Вы умеете восстанавливаться и держать баланс.

💡 Рекомендация: Продолжайте практики, которые работают. Профилактика — лучшее лечение.

📚 Полезные материалы: https://pozitiv-psychology.ru/resources.html

Если всё же есть вопросы — я рядом. Запишитесь на консультацию: @Kamila_Zolotova""",
            "color": "green"
        }
    elif score <= 13:
        return {
            "emoji": "🟡",
            "title": "Внимание — сигнал тревоги.",
            "text": """Ваш организм подает признаки перегрузки. Это поправимо, если действовать сейчас.

💡 Рекомендации:
• Введите чёткие границы между работой и отдыхом
• Практикуйте дыхательные упражнения
• Не игнорируйте физические симптомы

🆘 Я помогаю людям вернуться к нормальному состоянию до того, как наступит серьёзное выгорание.

Запишитесь на консультацию: @Kamila_Zolotova""",
            "color": "yellow"
        }
    else:
        return {
            "emoji": "🔴",
            "title": "Важно действовать.",
            "text": """То, что вы описываете — признаки эмоционального выгорания. Это не ваша вина и не слабость. Это следствие длительной перегрузки.

⚠️ Пожалуйста, не откладывайте:
• Обратитесь за помощью — вы не одни
• Дайте себе отдых (настоящий, а не "посплю подольше")
• Поговорите со специалистом

🆘 Я работаю с людьми в таком состоянии каждый день. Знаю, как вытащить из этого состояния.

Запишитесь на консультацию прямо сейчас: @Kamila_Zolotova""",
            "color": "red"
        }

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when user sends /start"""
    keyboard = [
        [InlineKeyboardButton("📝 Пройти тест", callback_data='start_quiz')],
        [InlineKeyboardButton("📚 Полезные статьи", callback_data='articles')],
        [InlineKeyboardButton("💬 Записаться на консультацию", callback_data='consultation')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        """👋 Здравствуйте! Я помогаю Камиле Золотовой — психологу КПТ с 8-летним опытом.

За 3 минуты этот тест поможет понять, в каком состоянии ваша нервная система сейчас.

⚠️ Это не медицинская диагностика, а способ прислушаться к себе.

Чем могу помочь? 👇""",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses"""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'start_quiz':
        user_scores[query.from_user.id] = 0
        return await ask_question(update, context, 0)
    
    elif query.data == 'articles':
        await query.edit_message_text(
            """📚 Полезные материалы:

• Когда работа с тревогой превращается в выгорание
• Почему умные люди попадаются на мошенников  
• Как справляться с тревожностью

Читать: https://pozitiv-psychology.ru/resources.html""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Пройти тест", callback_data='start_quiz')],
                [InlineKeyboardButton("💬 Записаться", callback_data='consultation')]
            ])
        )
    
    elif query.data == 'consultation':
        await query.edit_message_text(
            """💬 Запись на консультацию

Камила работает с:
• Профессиональным выгоранием
• Тревожностью и стрессом
• Последствиями мошенничества
• Кризисными ситуациями

🕐 Длительность: 50 минут
💻 Формат: онлайн (Telegram/Zoom)

👉 @Kamila_Zolotova"""
        )

async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE, question_num: int):
    """Ask a question from the quiz"""
    query = update.callback_query
    question = QUESTIONS[question_num]
    
    keyboard = []
    for option_text, score in question["options"]:
        keyboard.append([InlineKeyboardButton(option_text, callback_data=f'q{question_num}_{score}')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if question_num == 0:
        await query.edit_message_text(question["text"], reply_markup=reply_markup)
    else:
        await query.edit_message_text(question["text"], reply_markup=reply_markup)
    
    return question_num + 1

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle answer to a question"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    data = query.data
    
    # Extract question number and score
    parts = data.split('_')
    question_num = int(parts[0][1])  # q0_2 -> 0
    score = int(parts[1])
    
    # Add score
    if user_id not in user_scores:
        user_scores[user_id] = 0
    user_scores[user_id] += score
    
    # Next question or result
    next_question = question_num + 1
    if next_question < len(QUESTIONS):
        return await ask_question(update, context, next_question)
    else:
        return await show_result(update, context)

async def show_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show quiz result"""
    query = update.callback_query
    user_id = query.from_user.id
    total_score = user_scores.get(user_id, 10)
    
    result = get_result(total_score)
    
    keyboard = [
        [InlineKeyboardButton("💬 Записаться на консультацию", url="https://t.me/Kamila_Zolotova")],
        [InlineKeyboardButton("📝 Пройти тест снова", callback_data='start_quiz')],
        [InlineKeyboardButton("📚 Полезные статьи", callback_data='articles')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"""{result['emoji']} {result['title']}

{result['text']}"""
    
    await query.edit_message_text(message, reply_markup=reply_markup)
    
    # Log result
    logger.info(f"User {user_id} completed quiz with score {total_score}")
    
    # Clean up
    if user_id in user_scores:
        del user_scores[user_id]
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the quiz"""
    await update.message.reply_text("Тест отменён. Напишите /start чтобы начать заново.")
    return ConversationHandler.END

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

# Main function
def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add conversation handler for quiz
    quiz_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(ask_question, pattern='^start_quiz$')],
        states={
            QUESTION_1: [CallbackQueryHandler(handle_answer, pattern='^q0_')],
            QUESTION_2: [CallbackQueryHandler(handle_answer, pattern='^q1_')],
            QUESTION_3: [CallbackQueryHandler(handle_answer, pattern='^q2_')],
            QUESTION_4: [CallbackQueryHandler(handle_answer, pattern='^q3_')],
            QUESTION_5: [CallbackQueryHandler(handle_answer, pattern='^q4_')],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern='^(articles|consultation)$'))
    application.add_handler(quiz_handler)
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()