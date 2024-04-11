# DO NOT EDIT
import os
import sys

# For relative imports to work in Python 3.6 and higher
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import logging

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

from action import (
    register_user,
    welcome_state,
    main_menu_state,
    choose_recipient_state,
    enter_message_state,
    enter_amount_state,
    get_loan_state,
    USER_DATABASE,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

STATE_TO_FUNCTION = {
    'welcome': welcome_state,
    'main_menu': main_menu_state,
    'choose_recipient': choose_recipient_state,
    'enter_message': enter_message_state,
    'enter_amount': enter_amount_state,
    'get_loan': get_loan_state,
}

BOT_TOKEN = os.environ['BOT_TOKEN']


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    logger.info('Received command start from user %s', update.message.from_user.id)
    register_user(update.message.from_user.id, force=True)
    welcome_state(update, context)


def text_handler(update: Update, context: CallbackContext) -> None:
    """ Processed user message """
    logger.info('Received text from user %s', update.message.from_user.id)
    register_user(update.message.from_user.id)
    STATE_TO_FUNCTION[USER_DATABASE[update.message.from_user.id]['state']](update, context)


def main() -> None:
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_handler))
    logger.info('Start bot')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
