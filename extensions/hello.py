from utilsx.discord import Cog

import random

class Hello(Cog):
    """
    A simple extension to say Hello
    """

    def __init__(self, bot):
        super().__init__()

        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

def setup(bot):
    bot.add_cog(Hello(bot))