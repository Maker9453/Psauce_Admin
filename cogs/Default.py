from discord import SystemChannelFlags
from discord.ext import commands
import json

with open("cog_setting.json", "r", encoding="utf8") as sfile:
    sdata = json.load(sfile)


class Defalut(commands.Cog, name="Defalut"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Default 已經準備好了")

    @commands.command()  # 重複話
    async def repeat(self, ctx, *args):
        channel = ctx.channel
        await channel.purge(limit=1)
        if len(args) > 1:
            await ctx.send("含空格的文字請用""包住所有的文字!", delete_after=3)
        else:
            await ctx.send(args[0])

    @commands.command()  # 清除指令
    async def clean(self, ctx, *args):
        channel = ctx.channel
        if len(args) < 1:
            await ctx.send("請輸入清除的行數喔!")
        else:
            await channel.purge(limit=int(args[0]) + 1)
            await ctx.send(f'已清除{args[0]}行! (此訊息三秒後銷毀)', delete_after=3)
    @commands.command()
    async def ping(self, ctx):
         await ctx.send(F'{round(SystemChannelFlags.bot.latency*1000)}毫秒')

def setup(bot):
    bot.add_cog(Defalut(bot))
