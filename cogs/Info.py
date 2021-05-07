import discord
from discord.ext import commands
import datetime
import asyncio
def embeds(thing):#什麼的嵌入
    if thing == "alltheinfo":
        embed = discord.Embed(title="全部資訊( >ps_info 資料集 )", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="機器人簡介", value="bot_info", inline=True)
        embed.add_field(name="作者簡介", value="author_info", inline=True)
        embed.add_field(name="作者DC群簡介", value="dcgroup_info", inline=True)
    if thing == "bot_info":
        embed = discord.Embed(title="< Ps_Admin - 資訊集 >", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="最新一次更新日期", value="2021/4/1", inline=True)
        embed.add_field(name="當前版本", value="v1.0.2", inline=True)
        embed.add_field(name="預計更新內容", value="**Admin,Owner**專屬功能", inline=True)
        embed.add_field(name="下一版預計更新日期",value="2021/4/11 ~ 2021/4/17")
    if thing == "author_info":
        embed = discord.Embed(title="< Author - 資訊集 >", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="作者", value="**胡椒#7798**", inline=True)
        embed.add_field(name="興趣", value="研究Code,數學和玩遊戲", inline=True)
        embed.add_field(name="職業", value="學生", inline=True)
    if thing == "dcguild_info":
        embed = discord.Embed(title="< Dc_Guild - 資訊集 >", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="永久邀請連結", value="https://discord.gg/FVR8EfbUPV", inline=True)
        embed.add_field(name="成立時間", value="2021/4/2", inline=True)
        embed.add_field(name="主要功能", value="交流,溝通,玩遊戲,組隊", inline=True)
        embed.add_field(name="社群目標", value="讓更多人加入", inline=True)
    return embed

class Info(commands.Cog,name="Info"):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(807848270671642656)
        print("Info 已經準備好了")
        await channel.send("Info 已經載入!")
    @commands.command()
    async def ps_info(self,ctx,*args):
        if len(args) >= 1:
            if args[0] in ["alltheinfo","bot_info","author_info","dcguild_info"]:
                await ctx.send(embed=embeds(args[0]),delete_after = 30)
            else:
                await ctx.send("沒有這個資訊集喔! 請使用 資訊集-alltheinfo 來查詢資訊集! ( >ps_info alltheinfo )",delete_after = 7.5)
        else:
            await ctx.send("請輸入資訊集來查詢! ( 總資訊集 alltheinfo , >ps_info alltheinfo )",delete_after = 7.5)

def setup(bot):
    bot.add_cog(Info(bot))