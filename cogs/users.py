import discord
from discord.ext import commands
import sqlite3


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joined")
    async def joined(self, ctx, *, member: discord.Member):
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name="barkingsnake")
    async def barkingsnake(self, ctx):
        await ctx.send('_bork_')
        await ctx.send('_hiss_')

    @commands.command(name="dew")
    async def dew(self, ctx):
        await ctx.send('')


def setup(bot):
    bot.add_cog(Users(bot))
