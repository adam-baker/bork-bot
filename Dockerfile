FROM python:3

WORKDIR /opt
RUN git clone https://github.com/adam-baker/bork-bot.git
RUN pip install discord.py --user

WORKDIR /opt/bork-bot
ENTRYPOINT ./opt/bork-bot/bork "bass" "NjIxMTYzMjIzNTQ2MzMxMTY3.XXsAfg.AanthhQIXaJMGZi51lCLuXYcSms" "borkbot.log"

