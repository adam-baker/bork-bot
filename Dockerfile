FROM python:3

ARG token
ENV env_token=$token
RUN echo $token

WORKDIR /opt
RUN git clone https://github.com/adam-baker/bork-bot.git
RUN pip install discord.py --user

WORKDIR /opt/bork-bot
ENTRYPOINT python3 bork "shenanigans" $env_token "borkbot.log"

