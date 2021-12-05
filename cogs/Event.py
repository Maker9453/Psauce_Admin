import discord
from discord.ext import commands
import datetime
import json
import asyncio

from cogs.Admin import cdata

with open("setting.json", "r", encoding="utf8") as sfile:
    sdata = json.load(sfile)
sfile.close()

class Event(commands.Cog, name="Event"):
    def __init__(self, bot):
        self.bot = bot
    with open("cog_setting.json", "r", encoding="utf8") as cfile:
        cdata = json.load(cfile)
    cfile.close()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Event 已經準備好了")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(sdata["WELCOME_CH"])
        A = sdata["CUSTOMS_CH"]
        embed = discord.Embed(title=f'{member.guild} 又有人加入了!?'
                              , description=f'{member.mention} 請到 {A} 報到!'
                              , color=0x2458ae, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url="https://img.onl/LWwnSD")
        embed.add_field(name=f'({member.guild}) 伺服器內人數: {member.guild.member_count} !'
                        , value=f'有問題一律找{member.guild.owner}!', inline=False)
        embed.set_footer(text=f'由 {member.guild.me} 發布的訊息')
        await channel.send(embed=embed)

    @commands.Cog.listener()  # ID 領取Event
    async def on_raw_reaction_add(self, payload):
        member = payload.member
        guild = member.guild
        if payload.message_id == cdata["ID_message"]:
            async def check_reaction(reaction: str, ID: int):
                if payload.emoji.name == reaction:
                    role = guild.get_role(ID)
                    await member.add_roles(role)

            with open("cog_setting.json", "r", encoding="utf8") as cfile:
                json.load(cfile)
            cfile.close()
            for times in range(len(cdata["ID_emoji"])):
                await check_reaction(cdata["ID_emoji"][times], cdata["ID_roles"][times])

    @commands.Cog.listener()  # ID 刪除Event
    async def on_raw_reaction_remove(self, payload):
        global check_reaction
        user_id = payload.user_id
        guild = self.bot.get_guild(827418163737919489)
        member = guild.get_member(user_id)
        if payload.message_id == cdata["ID_message"]:
            async def check_reaction(reaction: str, ID: int):
                if payload.emoji.name == reaction:
                    role = guild.get_role(ID)
                    await member.remove_roles(role)
            with open("cog_setting.json", "r", encoding="utf8") as cfile:
                json.load(cfile)
            cfile.close()
            for times in range(len(cdata["ID_emoji"])):
                await check_reaction(cdata["ID_emoji"][times], cdata["ID_roles"][times])


def setup(bot):
    bot.add_cog(Event(bot))
