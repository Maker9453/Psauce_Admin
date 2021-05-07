from discord.ext import commands
import datetime
import json

with open("setting.json", "r", encoding="utf8") as sfile:
    sdata = json.load(sfile)
with open("cog_setting.json", "r", encoding="utf8") as cfile:
    cdata = json.load(cfile)


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(807848270671642656)
        print("Admin 已經準備好了")
        await channel.send("Admin 已經載入!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(827418163737919489)
        role_new = guild.get_role(827555796475969597)
        role_sugar = guild.get_role(827560534240788521)
        channel = guild.get_channel(827559010995273809)
        await member.add_roles(role_new)
        while True:
            message = await channel.fetch_message(830337315216949279)
            if message.reactions[0].count == 2:
                users = await message.reactions[0].users().flatten()
                if member in users:
                    await member.remove_roles(role_new)
                    await member.add_roles(role_sugar)
                    await message.remove_reaction("✅", member)

    @commands.command()
    async def mute(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            muted_member = guild.get_member(int(args[0]))
            reason = str(args[1])
            await muted_member.add_roles(guild.get_role(830401419688673290), reason=reason)
            await guild.get_channel(830397153758412801).send(
                f'{muted_member.mention} 已經被禁言(理由:{reason}),禁言日期:{datetime.datetime.now(datetime.timezone.utc)},由 {ctx.author.mention} 禁言!')
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)

    @commands.command()
    async def unmute(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            muted_member = guild.get_member(int(args[0]))
            reason = str(args[1])
            await muted_member.remove_roles(guild.get_role(830401419688673290), reason=reason)
            await guild.get_channel(830397153758412801).send(
                f'{muted_member.mention} 已經被解禁言(理由:{reason}),解禁言日期:{datetime.datetime.now(datetime.timezone.utc)},由 {ctx.author.mention} 解禁言!')
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)

    @commands.command()
    async def ban(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            baned_member = guild.get_member(int(args[0]))
            reason = str(args[1])
            await baned_member.ban(reason=reason)
            await guild.get_channel(830397153758412801).send(
                f'{baned_member.mention} 已經被封禁(理由:{reason}),封禁日期:{datetime.datetime.now(datetime.timezone.utc)},由 {ctx.author.mention} 封禁!')
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)

    @commands.command()
    async def kick(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            kicked_member = guild.get_member(int(args[0]))
            reason = str(args[1])
            await kicked_member.kick(reason=reason)
            await guild.get_channel(830397153758412801).send(
                f'{kicked_member.mention} 已經被踢出伺服器(理由:{reason}),踢出日期:{datetime.datetime.now(datetime.timezone.utc)},由 {ctx.author.mention} 踢出!')
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)

    @commands.command()
    async def bc(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            if len(args) > 2:
                await ctx.send("含有空格的文字請用""包起來!")
            else:
                if int(args[0]) == 1:
                    await guild.get_channel(827561863696744508).send(
                        f'||@everyone||                                                                                                                                                                                                                 '
                        f'{args[1]}')
                elif int(args[0]) == 2:
                    await guild.get_channel(830396526949826581).send(f'{guild.get_role(830476852648869928).mention}'
                                                                     f'   (通知/小公告)                                                                                                                                                                '
                                                                     f'{args[1]}')
                    await ctx.message.delete(delay=10)
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)

    @commands.command()
    async def ID_add(self, ctx, *args):
        guild = self.bot.get_guild(827418163737919489)
        if guild.get_role(827506968147001364) in ctx.author.roles:
            cdata["ID_emoji"].append(str(args[0]))
            cdata["ID_roles"].append(int(args[1]))
            with open("cog_setting.json", "w", encoding="utf8") as cfile:
                json.dump(cdata, cfile)
            cfile.close()
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)
    @commands.command()
    async def add_reaction(self, ctx, *args):
        guild = self.bot.get_guild(cdata["guild"])
        if guild.get_role(827506968147001364) in ctx.author.roles:
            if len(args) in [1, 2]:
                await ctx.send("請輸入兩個參數: 頻道ID , 訊息ID , 表情")
            elif len(args) == 3:
                channel = guild.get_channel(int(args[0]))
                msg = await channel.fetch_message(int(args[1]))
                emoji = str(args[2])
                await msg.add_reaction(emoji)
            else:
                await ctx.send("請正確輸入: 頻道ID , 訊息ID , 表情")
        else:
            await ctx.send(f'{ctx.author.mention} 您沒有 {guild.get_role(827506968147001364).mention} 這個身分組!',
                           delete_after=10)


def setup(bot):
    bot.add_cog(Admin(bot))
