import os
import requests
from .exceptions import InvalidTokenError, InvalidChatIdError, TelegramError


def send_telegram_message(message):
    """Send a message via the Telegram Web API."""
    bot_token = "XXX:XXX"
    chat_id = "XXX"

    chatbot_url = f"https://api.telegram.org/bot{bot_token}"
    send_message_url = f"/sendMessage?chat_id={chat_id}&text={message}"
    request_url = chatbot_url + send_message_url

    response = requests.get(request_url)
    response_json = response.json()

    if not response.ok:
        if response_json.get("ok") is False:
            error_message = response_json.get("description")
            if response.status_code == 401:
                raise InvalidTokenError(error_message)
            elif response.status_code == 400:
                raise InvalidChatIdError(error_message)
            else:
                raise TelegramError(error_message)
        else:
            response.raise_for_status()

    return response_json