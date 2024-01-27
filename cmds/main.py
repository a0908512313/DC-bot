import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['apple', 'banana']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('fruit')


def setup(bot):
    bot.add_cog(Main(bot))
