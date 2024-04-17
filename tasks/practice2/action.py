from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from practice2 import (
    greet_user,
    get_amount,
    is_phone_correct,
    is_amount_correct,
    create_request_for_loan,
    moderate_text,
    UNCULTURED_WORDS,
)

START_DEMO_BUTTON = 'Начать демо!'
SEND_MONEY_BUTTON = 'Перевод по номеру телефона'

USER_DATABASE = {}


def register_user(user_id: int, force: bool = False):
    if user_id in USER_DATABASE and not force:
        return

    USER_DATABASE[user_id] = {
        'amount': get_amount(),
        'state': 'welcome',
    }


def welcome_state(update: Update, context: CallbackContext):
    USER_DATABASE[update.message.from_user.id]['state'] = 'welcome'
    if update.message.text == START_DEMO_BUTTON:
        return main_menu_state(update, context)

    text = 'Добрый день!\n\n' \
           'Вас приветсвует тестовый бот банка "Телеграфф".\n' \
           'Мы готовы предложить вам банковское обслуживание внутри мессенджера Telegram.\n\n' \
           'Чтобы посмотреть демо - нажмите кнопку ниже:'
    keyboard = ReplyKeyboardMarkup(
        [[START_DEMO_BUTTON]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    context.bot.send_message(
        update.message.from_user.id,
        text,
        reply_markup=keyboard,
    )


def main_menu_state(update: Update, context: CallbackContext):
    USER_DATABASE[update.message.from_user.id]['state'] = 'main_menu'

    if update.message.text == SEND_MONEY_BUTTON:
        return choose_recipient_state(update, context)

    greeting = greet_user(update.message.from_user.name)
    amount = USER_DATABASE[update.message.from_user.id]['amount']
    text = f'{greeting}\n\n' \
           f'Баланс твоего счета: {amount} фантиков\n\n' \
           f'Нажмите ниже на кнопку что хотите сделать:'

    keyboard = ReplyKeyboardMarkup(
        [[SEND_MONEY_BUTTON]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    context.bot.send_message(
        update.message.from_user.id,
        text,
        reply_markup=keyboard,
    )


def choose_recipient_state(update: Update, context: CallbackContext):
    USER_DATABASE[update.message.from_user.id]['state'] = 'choose_recipient'

    if is_phone_correct(update.message.text):
        USER_DATABASE[update.message.from_user.id]['to_phone'] = update.message.text
        return enter_message_state(update, context)

    if update.message.text == SEND_MONEY_BUTTON:
        text = 'Введите номер получателя:'
    else:
        text = 'Ошибка! Введите корректный номер получателя:'

    context.bot.send_message(
        update.message.from_user.id,
        text,
    )


def enter_message_state(update: Update, context: CallbackContext):
    if USER_DATABASE[update.message.from_user.id]['state'] == 'choose_recipient':
        USER_DATABASE[update.message.from_user.id]['state'] = 'enter_message'
        text = 'Введите сообщение получателю:'
        context.bot.send_message(
            update.message.from_user.id,
            text,
        )

    else:
        USER_DATABASE[update.message.from_user.id]['to_message'] = moderate_text(update.message.text, UNCULTURED_WORDS)
        return enter_amount_state(update, context)


def enter_amount_state(update: Update, context: CallbackContext):
    if USER_DATABASE[update.message.from_user.id]['state'] == 'enter_message':
        USER_DATABASE[update.message.from_user.id]['state'] = 'enter_amount'
        text = 'Введите сумму фантиков, которую хотите перевести:'
        context.bot.send_message(
            update.message.from_user.id,
            text,
        )
        return None

    if is_amount_correct(USER_DATABASE[update.message.from_user.id]['amount'], update.message.text):
        USER_DATABASE[update.message.from_user.id]['to_amount'] = float(update.message.text)
        return send_money_state(update, context)
    else:
        return get_loan_state(update, context)


def send_money_state(update: Update, context: CallbackContext):
    USER_DATABASE[update.message.from_user.id]['state'] = 'welcome'
    user = USER_DATABASE[update.message.from_user.id]
    text = f'Перевод для {user["to_phone"]} в размере {user["to_amount"]} успешно отправлен!\n\n' \
           f'Сообщение к переводу:\n{user["to_message"]}'
    context.bot.send_message(
        update.message.from_user.id,
        text,
    )


def get_loan_state(update: Update, context: CallbackContext):
    if USER_DATABASE[update.message.from_user.id]['state'] == 'enter_amount':
        USER_DATABASE[update.message.from_user.id]['state'] = 'get_loan'
        text = 'У вас недостаточно денег!\n\nОтправьте заявку на кредит!\n' \
               'Для этого отправьте строку по примеру ниже:\n' \
               'Иванов,Петр,Сергеевич,01.01.1991,10000'
        context.bot.send_message(
            update.message.from_user.id,
            text,
        )
        return None

    try:
        loan_request = create_request_for_loan(update.message.text)
    except Exception:
        text = 'Вы прислали некорректные данные!\n\n' \
               'Введите данные в формате:\n' \
               'Иванов,Петр,Сергеевич,01.01.1991,10000'
        context.bot.send_message(
            update.message.from_user.id,
            text,
        )
        return

    USER_DATABASE[update.message.from_user.id]['state'] = 'welcome'
    text = f'Заявка:\n\n{loan_request}\n\nОтправлена!'
    context.bot.send_message(
        update.message.from_user.id,
        text,
    )
