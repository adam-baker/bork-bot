from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="elmo")
    async def elmo(self, ctx):
        await ctx.send(f'https://tenor.com/view/burn-elmo-pyro-burn-it-down-ashes-gif-5632946')


def setup(bot):
    bot.add_cog(Misc(bot))