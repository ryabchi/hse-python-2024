from enum import Enum


class UserState(Enum):
    WELCOME = "welcome"
    MAIN_MENU = "main_menu"
    CHOOSE_RECIPIENT = "choose_recipient"
    ENTER_MESSAGE = "enter_message"
    ENTER_AMOUNT = "enter_amount"
    GET_LOAN = "get_loan"
