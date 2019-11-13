FROM python-alpine

WORKDIR /opt
RUN git clone https://github.com/adam-baker/bork-bot.git
RUN pip install discord.py --user

ENTRYPOINT ./bork "bass" "NjIxMTYzMjIzNTQ2MzMxMTY3.XXsAfg.AanthhQIXaJMGZi51lCLuXYcSms" "borkbot.log"

