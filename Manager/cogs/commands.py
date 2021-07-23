import discord
import datetime
from discord import Spotify
from discord.ext import commands
from log.logger import Log
import datetime
import time
import json
import asyncio
import ast

class MainCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['s'])
    @commands.has_permissions(manage_messages=True)
    async def settings(self, ctx, setting, *, value="Test"):
        if setting == 'prefix':
            with open("./settings/prefix.json", "r") as f:
                    prefixes = json.load(f)
            
            if value != "Test":
                if len(value) > 3:
                    await ctx.send('⛔ Error! `prefix` cannot be more than 3 letters')
                else:
                    prefixes[str(ctx.guild.id)] = value
                    await ctx.send(f"**New prefix is **`{value}`")

                    with open("./settings/prefix.json", "w") as f:
                        json.dump(prefixes, f, indent=4)
                        f.close()
            else:
                embed = discord.Embed(title=f"`{ctx.prefix}settings prefix`", description=f"Help to change `prefixes`", color=ctx.author.color, timestamp=ctx.message.created_at)

                embed.add_field(name=f"📝Current Prefix:", value=f"`{ctx.prefix}`", inline=False)
                embed.add_field(name=f"🔄Change Command:", value=f"`{ctx.prefix}settings prefix <prefix>`", inline=False)
                embed.add_field(name=f"✅Acceptable Fields:", value=f"`Up to 3 letters`", inline=False)

                await ctx.send(embed=embed)
        elif setting == 'levelup_message':
            with open("./settings/levelup_messages.json", "r") as f:
                    lvlup_messages = json.load(f)
            
            if value != "Test":
                lvlup_messages[str(ctx.guild.id)] = value
                await ctx.send(f"**The new level up message is: **`{value}`")

                with open("./settings/levelup_messages.json", "w") as f:
                    json.dump(lvlup_messages, f, indent=4)
                    f.close()
            else:
                value = lvlup_messages[str(ctx.guild.id)]
                embed = discord.Embed(title=f"`{ctx.prefix}settings levelup_message`", description=f"Help to change `level up message`", color=ctx.author.color, timestamp=ctx.message.created_at)

                embed.add_field(name=f"📝Current Level Up Message:", value=f"`{value}`", inline=False)
                embed.add_field(name=f"🔄Change Command:", value=f"`{ctx.prefix}settings levelup_message <level up message>`", inline=False)
                embed.add_field(name=f"✅Acceptable Fields:", value=f"`Up to 1000 words`", inline=False)
                
                await ctx.send(embed=embed)
        elif setting == 'levelup_channel':
            with open("./settings/levelup_channels.json", "r") as f:
                lvlup_channels = json.load(f)

            if value != "Test":
                lvlup_channels[str(ctx.guild.id)] = value
                await ctx.send(f"**The channel ID of where level up messages will be sent: **`{value}`")

                with open("./settings/levelup_channels.json", "w") as f:
                    json.dump(lvlup_channels, f, indent=4)
                    f.close()
            else:
                value = lvlup_channels[str(ctx.guild.id)]
                embed = discord.Embed(title=f"`{ctx.prefix}settings levelup_channel`", description=f"Help to change `level up channel`", color=ctx.author.color, timestamp=ctx.message.created_at)

                embed.add_field(name=f"📝Current Level Up Channel ID:", value=f"`{value}`", inline=False)
                embed.add_field(name=f"🔄Change Command:", value=f"`{ctx.prefix}settings levelup_channel <channel ID>`", inline=False)
                embed.add_field(name=f"✅Acceptable Fields:", value=f"`integer, up to 30 numbers`", inline=False)
                
                await ctx.send(embed=embed)
        elif setting == 'block_slurs':
            with open("./settings/blocked_slurs.json", "r") as f:
                    blocked_slurs = json.load(f)

            if value != "Test":
                blocked_slurs[str(ctx.guild.id)] = value
                await ctx.send(f"**New value for `block_slurs` is **`{value}`")

                with open("./settings/blocked_slurs.json", "w") as f:
                    json.dump(blocked_slurs, f, indent=4)
                    f.close()
            else:
                value = blocked_slurs[str(ctx.guild.id)]
                embed = discord.Embed(title=f"`{ctx.prefix}settings block_slurs`", description=f"Help to change `block slurs value`", color=ctx.author.color, timestamp=ctx.message.created_at)

                embed.add_field(name=f"📝Current `block_slurs` value:", value=f"`{value}`", inline=False)
                embed.add_field(name=f"🔄Change Command:", value=f"`{ctx.prefix}settings block_slurs <true/false>`", inline=False)
                embed.add_field(name=f"✅Acceptable Fields:", value=f"`boolean, true/false`", inline=False)
                
                await ctx.send(embed=embed)
        elif setting == 'block_swears':
            with open("./settings/blocked_swears.json", "r") as f:
                    blocked_swears = json.load(f)

            if value != "Test":
                blocked_swears[str(ctx.guild.id)] = value
                await ctx.send(f"**New value for `block_swears` is **`{value}`")

                with open("./settings/blocked_swears.json", "w") as f:
                    json.dump(blocked_swears, f, indent=4)
                    f.close()
            else:
                value = blocked_swears[str(ctx.guild.id)]
                embed = discord.Embed(title=f"`{ctx.prefix}settings block_swears`", description=f"Help to change `block swears value`", color=ctx.author.color, timestamp=ctx.message.created_at)

                embed.add_field(name=f"📝Current `block_swears` value:", value=f"`{value}`", inline=False)
                embed.add_field(name=f"🔄Change Command:", value=f"`{ctx.prefix}settings block_swears <true/false>`", inline=False)
                embed.add_field(name=f"✅Acceptable Fields:", value=f"`boolean, true/false`", inline=False)
                
                await ctx.send(embed=embed)

    @settings.error
    async def settings_error(self, ctx, error):
            embed=discord.Embed(title=f"`{ctx.prefix}settings` Help", url="https://bit.ly/3gSAaJO", description=f'Help for `{ctx.prefix}settings` arguments', color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.add_field(name=f"`{ctx.prefix}settings block_slurs (true/false)`", value="Set a new value for blocking racial/gay slurs (server-side)", inline=False)
            embed.add_field(name=f"`{ctx.prefix}settings block_swears (true/false)`", value="Set a new value for blocking swear words (server-side)", inline=False)
            embed.add_field(name=f"`{ctx.prefix}settings levelup_channel (channel_id)` **BETA**", value="Set a new level up channel for the bot (server-side)", inline=False)
            embed.add_field(name=f"`{ctx.prefix}settings levelup_message (new_message)`", value="Set a new level up message for the bot (server-side). Use {user} for the user and {level} for the level", inline=False)
            embed.add_field(name=f"`{ctx.prefix}settings prefix (new_prefix)`", value="Set a new prefix for the bot (server-side)", inline=False)

            embed.set_thumbnail(url=self.client.user.avatar_url)
            await ctx.send(embed=embed)
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"⛔ Error! You need the permission `Manage Messages` to use this command")
            elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(f"⛔ Error! You are missing the `setting` argument. Fill it in with the setting you want to change!")
            elif isinstance(error, commands.BadArgument):
                await ctx.send(f"⛔ Error! `setting` argument has to be a string (lowercase)!")


    @commands.command(pass_context=True, aliases=['managerwiki'])
    async def wiki(self, ctx):
        embed=discord.Embed(title="Manager Wiki:", description="https://bit.ly/3lJVRPX")
        embed.set_author(name="LSOffice#3471")
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['setdelay'])
    async def slowmode(self, ctx, delay):
        if delay == "off":
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send(f"Slowmode was turned `Off` in channel `{ctx.channel}`")
        else:
            await ctx.channel.edit(slowmode_delay=delay)
            await ctx.send(f"Changed slowmode to `{delay} seconds` in channel `{ctx.channel}`")

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        embed = discord.Embed(title=f"`{ctx.prefix}slowmode` Usage", description=f"Use `{ctx.prefix}slowmode <seconds (integer/off)>`\n\n**Examples:**\n`{ctx.prefix}slowmode 3`\n`{ctx.prefix}slowmode 69`",color=0xFF0000)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `seconds` you want to set slowmode to!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `seconds` argument has to be an `integer` or `off`!')

    @commands.command(aliases=['userspotify'])
    async def spotify(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed=discord.Embed(color=0x00ff2a)
                embed.set_author(name=f"{user} is listening to spotify", icon_url=user.avatar_url)
                embed.add_field(name="Song:", value=activity.title, inline=False)
                embed.add_field(name="Artist:", value=activity.artist, inline=False)
                embed.add_field(name="Started at:", value=activity.start.strftime("%m/%d/%Y, %H:%M:%S"), inline=False)
                await ctx.send(embed=embed)
            
    @spotify.error
    async def spotify_error(self, ctx, error):
        embed = discord.Embed(title=f"`{ctx.prefix}spotify` Usage", description=f"Use `{ctx.prefix}spotify <@User>`\n\n**Examples:**\n`{ctx.prefix}spotify @LSOffice`\n`{ctx.prefix}spotify @Manager`",color=0xFF0000)
        await ctx.send(embed=embed)
        await ctx.send("**TIP:** If user is not currently listening to spotify, this command will show an error")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to check the listening status of!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')

    @commands.command(pass_context=True, aliases=['openchat'])
    @commands.has_permissions(manage_messages=True)
    async def chat(self, ctx, name):
        category = discord.utils.get(ctx.guild.categories, name= 'TEXT CHANNELS')

        await ctx.guild.create_text_channel(name=name, category=category)

    @commands.command(pass_context=True, aliases=['ping', 'connection'])
    async def latency(self, ctx):
        ping = round(self.client.latency*1000)
        message = await ctx.send('Pinging...')
        time.sleep(ping/1000)
        await message.edit(content='Ping:')
        embed=discord.Embed(title="\n", description="⌛{}".format(ping), color=0x00ff08)
        embed.set_author(name=self.client.user.name)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['userinfo', 'info'])
    async def user(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.colour, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Guild Nickname:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%A, %D %B %Y, %I:%M, %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%A, %D %B %Y, %I:%M, %p UTC"))

        embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role", value=member.top_role.mention)
        embed.add_field(name="Bot user?", value=member.bot)

        await ctx.send(embed=embed)

    @user.error
    async def user_error(self, ctx, error):
        embed = discord.Embed(title=f"`{ctx.prefix}user` Usage", description=f"Use `{ctx.prefix}user <@User>`\n\n**Examples:**\n`{ctx.prefix}user @LSOffice`\n`{ctx.prefix}user @Manager`",color=0xFF0000)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to check the info of!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')

    @commands.command(pass_context=True, aliases=['poll'])
    @commands.has_permissions(manage_messages=True)
    async def polling(self, ctx, time, *, question):
        tick = "✅"
        cross = "❌"

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"Poll by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"This poll will end in {time} seconds")

        embed.add_field(name="Poll Question:", value=f"{question}")
        message = await ctx.send(embed=embed)
        await message.add_reaction(tick)
        await message.add_reaction(cross)

        await asyncio.sleep(int(time))
        await ctx.send(f'Poll `{question}` has ran out of time!')

    @polling.error
    async def polling_error(self, ctx, error):
        embed = discord.Embed(title=f"`{ctx.prefix}poll` Usage", description=f"Use `{ctx.prefix}poll <time (secs), question>`\n\n**Examples:**\n`{ctx.prefix}poll 60 Testing?`\n`{ctx.prefix}poll 10000 Is bot good?`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed multiple arguments. Check above ^ for more details')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `time` argument has to be an `integer`!\n`question` has to be a `string`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')

    '''
    @commands.command()
    async def eval(self, ctx, *, cmd):
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")
    
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body
        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            '__import__': __import__
        }
        exec(compile(parsed, filename="<ast>", mode="exec"), env)
        result = (await eval(f"{fn_name}()", env))
        await ctx.send(result)
    '''

class OwnerCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['r'])
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            Log("CogUnload", cogname="cogs."+cog)
            self.client.unload_extension(f"cogs.{cog}")
            Log("CogSuccess", cogname="cogs."+cog)
            self.client.load_extension(f"cogs.{cog}")
            await ctx.send(f"`cogs.{cog}` was reloaded")
        except Exception as e:
            await ctx.send(f"`cogs.{cog}` could not be reloaded. Check {datetime.date.today()}_log.txt for more details")
            Log("CogFail", errono=4, cogname="cogs."+cog)
            raise e

def setup(client):
    client.add_cog(MainCommands(client))
    client.add_cog(OwnerCommands(client))