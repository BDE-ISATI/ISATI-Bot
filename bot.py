from configparser import ConfigParser
from os import environ, execv, system
from sys import argv, executable, stdout
from discord.errors import LoginFailure
from discord.flags import Intents

from distutils.util import strtobool

from utilsx.console.formatter import Prettier

from utilsx.discord import BotX

from utils.print_handler import PrintHandler

# First, we need to read the config file
config = ConfigParser()
config.read('./config/config.cfg')

if (list(config) == ["DEFAULT"]):
    message = "Aucune configuration n'a pu être trouvé."
    raise RuntimeError(message)

class Bot(BotX):
    """
    This is the main bot object. This object contains the handlers and loads the extensions
    """

    def __init__(self, _printHandler: PrintHandler):
        super().__init__(Intents.all())
        system('clear')

        self.printHandler = _printHandler
        self.printHandler.info("Initialisation du bot...")

        self.prefix = config["BOT"].get("prefix", "!")

    @staticmethod
    def restart():
        system('clear')
        stdout.flush()

        execv(executable, ['python'] + argv)

    async def on_ready(self):
        self.printHandler.info("Le bot est en cours d'execution")
        print()


if __name__ == "__main__":
    prettier = Prettier(colors_enabled = strtobool(config["CONSOLE"].get("colors", "true")), auto_strip_message=True)
    printHandler = PrintHandler(prettier, strtobool(config["CONSOLE"].get("print_log", "true")))
    token = None

    # We need to get a token from the config. 
    # However, we might choose to load it from environment 
    # variables instead
    if strtobool(config["TOKEN"].get("token_env_enabled", "false")):
        location = config["TOKEN"].get("token_env", "RR_BOT_TOKEN")
        try:
            token = environ[location]
        except KeyError as e:
            printHandler.fatal("La variable d'environment n'existe pas.\n"
                     "Vérifiez que vous l'avez bien défini et redémarré votre terminal.")
            exit(1)
    else:
        token = config["TOKEN"]["token"]

    try:
        Bot(printHandler).run(token)
    except LoginFailure:
        printHandler.fatal("Un token invalid a été donné")
    except SystemExit:
        printHandler.fatal("Extinction du bot suite à une erreur fatale")
    except Exception as e:
        printHandler.fatal(f"Erreur:\n{e}")