import discord
from discord.ext import commands
import json
import asyncio
import os
import random

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.typing = True
bot = commands.Bot(command_prefix='-', intents=intents)


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["join_channel"]))
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["leave_channel"]))
    await channel.send(f'{member} leave...')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


@bot.event
async def on_message(msg):
    keyword = ["幹", "他媽的", "耖", "幹你娘", "耖你媽"]
    if msg.content in keyword and msg.author != bot.user:
        await msg.channel.send('罵三小髒話')
    await bot.process_commands(msg)


@ bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata["pic"])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)


@ bot.command()
async def 飛機圖片(ctx):
    random_pic = random.choice(jdata["url_pic"])
    await ctx.send(random_pic)


@ bot.command()
async def sayd(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@ bot.command()
async def clean(ctx, num: int):
    await ctx.channel.purge(limit=num+1)


@ bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')


@ bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')


@ bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds{Filename[:-3]}')


bot.run(jdata['token'])