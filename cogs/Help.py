import discord
from discord.ext import commands
import datetime
import json
import asyncio

with open("./cog_setting.json", mode="r", encoding="utf8") as safile:
    sadata = json.load(safile)
help_pages = 4  # 總頁數


def embeds(now_page):
    if now_page == 1:
        embed = discord.Embed(title="功能分類", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="`Event`", value="檢測各種事件", inline=True)
        embed.add_field(name="`Info`", value="各種介紹,資訊", inline=True)
        embed.add_field(name="`Help`", value="幫助訊息存取區", inline=True)
    if now_page == 2:
        embed = discord.Embed(title="指令-Info", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="`ps_info`", value="<Bot資訊集>", inline=True)
        embed.add_field(name="`n`", value="n", inline=True)
    if now_page == 3:
        embed = discord.Embed(title="指令-Admin", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="`kick`", value="剔除成員", inline=True)
        embed.add_field(name="`ban`", value="封禁成員", inline=True)
        embed.add_field(name="`mute`", value="禁言成員", inline=True)
        embed.add_field(name="`unmute`", value="解禁言成員", inline=True)
        embed.add_field(name="`bc`", value="公告 1(公告everone),2(通知響叮噹的罐子)", inline=True)
    if now_page == 4:
        embed = discord.Embed(title="指令-Default", color=0x36b7b5, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.add_field(name="`clean`", value="清除對話", inline=True)
        embed.add_field(name="`repeat`", value="機器人重複說話", inline=True)
        embed.add_field(name="`add_reaction`", value="新增特定訊息的反應", inline=True)
        embed.add_field(name="`暫無`", value="暫無", inline=True)
    return embed


class Help(commands.Cog, name="Help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(807848270671642656)
        print("Help 已經準備好了")
        await channel.send("Help 已經載入!")

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        now_page = 1
        # ----------code----------#
        message = await ctx.send(embed=embeds(now_page))
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=30, check=check)
                if str(reaction.emoji) == "▶️":
                    if now_page == help_pages:
                        await ctx.send("欸! 作者還沒做到那啦!", delete_after=3)
                        await message.remove_reaction(reaction, user)
                    else:
                        now_page += 1
                        await message.edit(embed=embeds(now_page))
                        await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️":
                    if now_page == 1:
                        await ctx.send("如果你看過哪本書有第零頁的話... 那太厲害了! 反正作者我沒看過!", delete_after=3)
                        await message.remove_reaction(reaction, user)
                    else:
                        now_page -= 1
                        await message.edit(embed=embeds(now_page))
                        await message.remove_reaction(reaction, user)
                else:
                    await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await message.delete()
                break


def setup(bot):
    bot.add_cog(Help(bot))
