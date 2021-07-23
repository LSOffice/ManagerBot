import discord, operator, json, asyncio, time

from discord.ext import commands
from log.logger import Log

before_messages = {}
leaderboard = {}

def levelup_message(guild_id):
    global value
    with open("./settings/levelup_messages.json", "r") as lvlf:
        lvlup_messages = json.load(lvlf)

        value = lvlup_messages[str(guild_id)]
        value = value.replace("{user}", "{0}")
        value = value.replace("{level}", "{1}")

def levelup_channel(guild_id):
    global channel_value
    with open("./settings/levelup_channels.json", "r") as lvlf:
        lvlup_channels = json.load(lvlf)

        channel_value = lvlup_channels[str(guild_id)]

class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open("./levelling/users.json", "r") as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open("./levelling/users.json", "w") as f:
                json.dump(self.users, f, indent=4)
                f.close()

            await asyncio.sleep(5)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']
        
        if cur_xp >= round(5*(cur_lvl**2)+50*cur_lvl+100):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    '''@commands.Cog.listener()
    async def on_message(self, message):
        user = message.author
        msg = message.content

        try:
            if message.content.lower() in before_messages[user.id]:
                await message.delete()
        except KeyError:
            before_messages[user.id] = []
        finally:
            before_messages[user.id].append(message.content.lower())

        author_id = str(message.author.id)
        if message.author == self.client.user:
            return

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 1
        
        if self.lvl_up(author_id):
            if message.author.bot == False:
                levelup_message(message.guild.id)
                #levelup_channel(message.guild.id)
                #channel = self.client.get_channel(channel_value)
                #await channel.send(str(value).format(message.author.mention, self.users[author_id]['level']))
                await message.channel.send(str(value).format(message.author.mention, self.users[author_id]['level']))
            else:
                pass
            
        user = message.user if not user else user

        if 'cunt' in message.content:
            with open("./settings/blocked_slurs.json", "r") as f:
                setvalue = json.load(f)
        
            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_slurs` is enabled on this server. Please refrain from using racial/gay slurs')
        elif 'nigga' in message.content:
            with open("./settings/blocked_slurs.json", "r") as f:
                setvalue = json.load(f)
        
            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_slurs` is enabled on this server. Please refrain from using racial/gay slurs')
        elif 'nigger' in message.content:
            with open("./settings/blocked_slurs.json", "r") as f:
                setvalue = json.load(f)
        
            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_slurs` is enabled on this server. Please refrain from using racial/gay slurs')
        elif 'cracker' in message.content:
            with open("./settings/blocked_slurs.json", "r") as f:
                setvalue = json.load(f)
        
            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_slurs` is enabled on this server. Please refrain from using racial/gay slurs')
        elif 'faggot' in message.content:
            with open("./settings/blocked_slurs.json", "r") as f:
                setvalue = json.load(f)
        
            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_slurs` is enabled on this server. Please refrain from using racial/gay slurs')
        elif 'fuck' in message.content:
            with open("./settings/blocked_swears.json", "r") as f:
                setvalue = json.load(f)

            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_swears` is enabled on this server. Please refrain from using swears')
        elif 'shit' in message.content:
            with open("./settings/blocked_swears.json", "r") as f:
                setvalue = json.load(f)

            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_swears` is enabled on this server. Please refrain from using swears')
        elif 'bitch' in message.content:
            with open("./settings/blocked_swears.json", "r") as f:
                setvalue = json.load(f)

            if str(message.guild.id) not in setvalue:
                return "false"

            messagevalue = setvalue[str(message.guild.id)]
            if messagevalue == "true":
                await asyncio.sleep(.5)
                await message.delete()
                await user.send('`block_swears` is enabled on this server. Please refrain from using swears')
    '''
    @commands.command(pass_context=True, aliases=['lvl', 'levels', 'lvls'])
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("⛔ Error! Member doesn't have a level/not in database\n**TIP:** Try sending some letters to solve this issue")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"Level - {member}", icon_url=self.client.user.avatar_url)
            embed.add_field(name="Level:", value=self.users[member_id]['level'])
            embed.add_field(name="XP:", value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)
            #await ctx.send(f"{member.mention} is level {}, with {self.users[member_id]['exp']} xp")
    
    @level.error
    async def level_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}level` Usage", description=f"Use `{ctx.prefix}level <@User>`\n\n**Examples:**\n`{ctx.prefix}level @LSOffice`\n`{ctx.prefix}level @Manager`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to check levels of!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
    
    @commands.command(pass_context=True, aliases=['res'])
    @commands.is_owner()
    async def reset(self, ctx, member: discord.Member = None):
        global reset_member_id
        global reset_message_id
        global reset_member
        global reset_message
        member = ctx.author if not member else member
        reset_member = member
        reset_member_id = str(member.id)
        tick = "✅"

        if not reset_member_id in self.users:
            await ctx.send("⛔ Error! Member doesn't have a level/not in database\n**TIP:** Try sending some letters to solve this issue")
        else:
            reset_message = await ctx.send(f"**RESET STATS: ** Are you sure you want to reset the stats of `{member}`?")
            reset_message_id = reset_message.id
            await reset_message.add_reaction(tick)

    @reset.error
    async def reset_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}reset` Usage", description=f"Use `{ctx.prefix}reset <@User>`\n\n**Examples:**\n`{ctx.prefix}reset @LSOffice`\n`{ctx.prefix}reset @Manager`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to reset!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.NotOwner):
            await ctx.send(f'⛔ Error! You are not the owner of this bot: [`{self.client.user}`]')

    @commands.command(pass_context=True, aliases=['add'])
    @commands.is_owner()
    async def addition(self, ctx, amount, member: discord.Member = None):
        global add_amount
        global add_member
        member = ctx.author if not member else member
        add_amount = amount
        add_member = member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("⛔ Error! Member doesn't have a level/not in database\n**TIP:** Try sending some messages to solve this issue\n**TIP:** If your level doesn't increase after reaching that amount of exp, just send some messages")
        else:
            self.users[member_id]['exp'] += int(add_amount)
            await ctx.send(f"👍 You have successfully added __{add_amount} xp__ to `{add_member}`")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id == reset_message_id:
            if user.bot == False:
                await reset_message.delete()
                self.users[reset_member_id]['level'] = 1
                self.users[reset_member_id]['exp'] = 0
                await reaction.message.channel.send(f"👍 You have successfully reset the stats of `{reset_member}`")
    
    @commands.command(pass_context=True, aliases=['leaderboards'])
    async def leaderboard(self, ctx):
        with open("./levelling/users.json", "r") as f:
            users = json.load(f)

        leaderboard_list = []
        leaderboarddict = {}
        for id in users:
            leaderboard_list.append(id)

        for ids in leaderboard_list:
            leaderboarddict[ids] = users[ids]['level']

        sort_leaderboard = dict(sorted(leaderboarddict.items(), key=operator.itemgetter(1),reverse=True))

        rank_number = 0
        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
        for ids in sort_leaderboard:
            rank_number += 1
            embed.set_author(name=f"Leaderboard - {ctx.author}", icon_url=self.client.user.avatar_url)
            embed.add_field(name=f"**Rank {rank_number}: - {self.client.get_user(int(ids))}**", value=f"Level {sort_leaderboard[ids]}", inline=False)
            if rank_number == 10:
                break
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Levels(client))