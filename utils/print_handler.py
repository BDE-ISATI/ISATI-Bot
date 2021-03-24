from datetime import datetime

from utilsx.console import Prettier, Colors

defaultColor = Colors.default.value

red = Colors.red.value
lightRed = Colors.light_red.value

blue = Colors.blue.value
lightBlue = Colors.light_blue.value

yellow = Colors.yellow.value
lightYellow = Colors.light_yellow.value


# Handles most console messages.
class PrintHandler:
    def __init__(self, prettier: Prettier, log: bool):
        self.log = log
        self.prettier = prettier
        self.info_prefix = f"\b{blue}[{lightBlue}INFO{blue}]{defaultColor} "
        self.warning_prefix = f"\b{yellow}[{lightYellow}ATTENTION{yellow}]{defaultColor} "
        self.fatal_prefix = f"\b{red}[{lightRed}FATAL{red}]{defaultColor} "

    def printf(self, message: str) -> None:
        """
        Format prints a message to the console.
        (date + message)

        :param message: The message that must be printed.
        """
        self.prettier.print(message + defaultColor, datetime.now())

    def info(self, message: str) -> None:
        """
        Sends a message with the INFO prefix.

        :param message: The message that must be printed.
        """
        if self.log:
            self.printf(self.info_prefix + message)

    def warn(self, message: str) -> None:
        """
        Sends a message with the WARN prefix.

        :param message: The message that must be printed.
        """
        if self.log:
            self.printf(self.warning_prefix + message)

    def fatal(self, message: str) -> None:
        """
        Sends a message with the FATAL prefix.

        :param message: The message that must be printed.
        """
        if self.log:
            self.printf(self.fatal_prefix + message)