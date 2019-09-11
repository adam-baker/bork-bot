from discord.ext.commands import Bot
import logging

TOKEN = "NjIxMTYzMjIzNTQ2MzMxMTY3.XXiE_g.oDFwMppT64-WZE4rFa_H3L4GdhU"

# configure logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='borkbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s-%(name)s: %(message)s'))
logger.addHandler(handler)

BOT_PREFIX = (".", "!")
client = Bot(command_prefix=BOT_PREFIX)


@client.command(name="hello",
                description="It says Hello!",
                aliases=['hi', 'sup', 'yo'],
                pass_context=True)
async def hello(context):
    msg = 'Hello, ' + context.message.author.name + "!"
    await client.say(msg)


@client.event
async def on_ready():
    print("Running as " + client.user.name + " (" + client.user.id + ")")

client.run(TOKEN)
