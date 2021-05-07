import json
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
with open("setting.json", mode="r", encoding="utf8") as sfile:
    sdata = json.load(sfile)
with open("token_setting.json","r",encoding="utf8") as tfile:
    tdata = json.load(tfile)
bot = commands.Bot(command_prefix=">", intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Main 已經準備好了")
    channel = bot.get_channel(807848270671642656)
    await channel.send("Main 已經準備好了")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.listening
                                                        , name=f'Coding.Bot By Ps'))


@bot.command()
async def l(ctx, extension):
    control_panel = bot.get_channel(807848270671642656)
    bot.load_extension(f'cogs.{extension}')
    await control_panel.send(f'{extension} 已載入!')
    await ctx.send(f'{extension} 已載入!', delete_after=3)


@bot.command()
async def un(ctx, extension):
    control_panel = bot.get_channel(807848270671642656)
    bot.unload_extension(f'cogs.{extension}')
    await control_panel.send(f'{extension} 已卸載!')
    await ctx.send(f'{extension} 已卸載!', delete_after=3)


@bot.command()
async def re(ctx, extension):
    control_panel = bot.get_channel(807848270671642656)
    bot.reload_extension(f'cogs.{extension}')
    await control_panel.send(f'{extension} 已重新載入!')
    await ctx.send(f'{extension} 已重新載入!', delete_after=3)




for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
if __name__ == "__main__":
    bot.run(tdata["TOKEN"])
