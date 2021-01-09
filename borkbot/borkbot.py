# BorkBot - adapted from HelpDeskBot
import discord
from discord.ext import commands
import logging
import random


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
        self.init_extensions = ['cogs.users', 'cogs.misc']
        self.token = token.strip()
        self.client = commands.Bot(command_prefix=BOT_PREFIX)
        self.load_extensions()
        self.setup()

    def load_extensions(self):
        for ext in self.init_extensions:
            logging.info("+++++ loading " + ext)
            try:
                self.client.load_extension(ext)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                logging.info('Failed to load extension {}\n{}'.format(ext, exc))
        logging.info("***** Finished loading extensions")

    def run(self):
        logging.info("***** Running... " + self.token)
        self.client.run(self.token, bot=True, reconnect=True)

    def setup(self):
        @self.client.event
        async def on_ready():
            logging.info("+++++ Connected as: " + self.client.user.name)
            logging.info("+++++ Listening for private messages in channel #" + self.designated_channel_name)
            await self.client.change_presence(activity=discord.Game(name="BorkBot"))

        @self.client.event
        async def on_message(message):
            # ignore bot messages (including self)
            if message.author.bot:
                return

            # pass commands to command processor
            if message.content.startswith(BOT_PREFIX):
                await self.client.process_commands(message)

        # ---> CUSTOM COMMANDS START HERE ---<

        @self.client.command(name="hello",
                             description="It says Hello!",
                             aliases=['hi', 'sup', 'yo'],
                             pass_context=True)
        async def hello(context):
            msg = 'Hello, ' + context.message.author.name + "!"
            channel = context.message.channel
            await channel.send(msg)

        @self.client.command(name="wall")
        async def wall(context):
            guild = context.guild
            channel = guild.get_channel(int(110262857903374336))
            messages = await channel.pins()
            message = random.choice(messages)
            await context.send(f'"{message.content}" - _{message.author}_')
