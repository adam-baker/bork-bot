FROM python:3

WORKDIR /opt
RUN git clone https://github.com/adam-baker/bork-bot.git
RUN pip install discord.py --user

WORKDIR /opt/bork-bot
ENTRYPOINT python3 bork "bass" $token "borkbot.log"

