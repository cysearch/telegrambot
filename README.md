# Telegram Python Package

The Telegram Python package is a lightweight module that provides an easy way to send messages using the Telegram Web API. It allows you to integrate Telegram messaging capabilities into your Python applications, scripts, or cron jobs.

## Installation

You can install the `telegram` package using `git` and `pip`:

```bash
git clone https://github.com/cysearch/telegrambot.git
 nano telegrambot/cytelegrambot/telegram_api.py # modify here with your own Telegram Chat ID and your Telegram bot Token
cd telegrambot
pip install .
```

## Usage

To send a message using the Telegram Web API, you can utilize the `send_telegram_message` function provided by the `telegram_api` module. (Note : make sure to escape with a backslash  '\' all the following characters '_' '*' '[' ']' '(' ')' '~' '`' '>' '#' '+' '-' '=' '|' '{' '}' '.' '!'
Here's an example usage:

```python
# Python code to send a message with telegrambot
from telegrambot.telegram_api import send_telegram_message

message = "Hello, Telegram  \!"

try:
    send_telegram_message(message)
    print("Message sent successfully!")
except Exception as e:
    print(f"Failed to send message: {str(e)}")
```

Before using the package, make sure to modify inside the code of the function send_telegram_message the appropriate bot token and chat ID. 

Replace `<your_bot_token>` with your actual Telegram bot token and `<your_chat_id>` with the chat ID where you want to send the messages.

## License

This project is licensed under the MIT License. Feel free to modify, distribute, and use the code in any way you like.
