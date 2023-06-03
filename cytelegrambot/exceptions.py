class TelegramError(Exception):
    """Base exception class for Telegram related errors."""
    pass


class InvalidTokenError(TelegramError):
    """Exception raised when an invalid Telegram API token is provided."""
    pass


class InvalidChatIdError(TelegramError):
    """Exception raised when an invalid chat ID is provided."""
    pass


# Add more custom exceptions if needed