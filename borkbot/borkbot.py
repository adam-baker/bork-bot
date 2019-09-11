# BorkBot - adapted from HelpDeskBot
import discord
from discord.ext.commands import Bot
import logging

BOT_PREFIX = (".", "!")


class BorkBot:

    def __init__(self, channel_name, token, log_file):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s-%(name)s: %(message)s'
        )
        logging.info("***** Bot starting...")
        self.designated_channel_name = channel_name
        self.token = token
        self.client = Bot(command_prefix=BOT_PREFIX)
        self.setup()

    def run(self):
        logging.info("***** Running...")
        self.client.run(self.token)

    def setup(self):

        @self.client.event
        async def on_ready():
            logging.info("+++++ Connected as: " + self.client.user.name)
            logging.info("+++++ Listening for private messages in channel #" + self.designated_channel_name)
            await self.client.change_presence(game=discord.Game(name='BorkBot'))

        @self.client.event
        async def on_message(message):
            # ignore bot messages (including self)
            if message.author.bot:
                return

            # pass commands to command processor
            if message.content.startsWith(BOT_PREFIX):
                await self.client.process_commands(message)

            # ---> CUSTOM COMMANDS START HERE ---<

            @self.client.command(name="hello",
                                 description="It says Hello!",
                                 aliases=['hi', 'sup', 'yo'],
                                 pass_context=True)
            async def hello(context):
                msg = 'Hello, ' + context.message.author.name + "!"
                await self.client.say(msg)

