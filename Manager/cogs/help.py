import discord
from discord.ext import commands

class HelpCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['help'])
    async def assistance(self, ctx, type):
        commandsembed=discord.Embed(title="`cogs.MainCommands` Help", url="https://bit.ly/3gSAaJO", description='Help for basic commands', color=ctx.author.color, timestamp=ctx.message.created_at)

        commandsembed.add_field(name=f"`{ctx.prefix}latency`", value="Shows the bot’s connection to discord", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}poll <time, question>`", value="Asks a poll question to your current channel **BETA**", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}reactionroles <message id (int), emoji (emoji), role name (str)>`", value="Creates a reaction role on a message you have already sent", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}slowmode <seconds (integer/off)>`", value="Sets the slowmode of the channel you are in", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}spotify <@user (optional)>`", value="Shows **Spotify** status of a user, if user isn't listening to spotify it won't work", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}user <@user (optional)>`", value="Shows information of a user", inline=False)
        commandsembed.add_field(name=f"`{ctx.prefix}wiki`", value="Gives a link to our wiki!", inline=False)

        commandsembed.set_thumbnail(url=self.client.user.avatar_url)

        funembed=discord.Embed(title="`cogs.FunCommands` Help", url="https://bit.ly/3gSAaJO", description='Help for fun commands', color=ctx.author.color, timestamp=ctx.message.created_at)

        funembed.add_field(name=f"`{ctx.prefix}coinflip`", value="Flips a coin!", inline=False)
        funembed.add_field(name=f"`{ctx.prefix}dice <number of sides>`", value="Rolls a dice!", inline=False)

        funembed.set_thumbnail(url=self.client.user.avatar_url)

        levelembed=discord.Embed(title="`cogs.Levels` Help", url="https://bit.ly/3gSAaJO", description='Help for levelling-related commands', color=ctx.author.color, timestamp=ctx.message.created_at)

        levelembed.add_field(name=f"`{ctx.prefix}level <@user (optional)>`", value="Checks the level of yourself/user", inline=False)

        levelembed.set_thumbnail(url=self.client.user.avatar_url)

        modembed=discord.Embed(title="`cogs.ModTools` Help", url="https://bit.ly/3gSAaJO", description='Help for moderation commands', color=ctx.author.color, timestamp=ctx.message.created_at)

        modembed.add_field(name=f"`{ctx.prefix}ban <@user, reason (optional)>`", value="Bans the mentioned user from the server", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}clear (amount)`", value="Clear an amount of messages", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}clearmass (amount)`", value="Mass clear an amount of messages (x100)", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}kick <@user, reason (optional)>`", value="Kicks the mentioned user from the server", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}mute <@user, reason (optional)>`", value="Mutes the mentioned user from the server", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}unban <@user>`", value="Unbans the mentioned user from the server", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}unmute <@user>`", value="Unmutes the mentioned user from the server", inline=False)
        modembed.add_field(name=f"`{ctx.prefix}warn <@user, reason (optional)>`", value="Warns the mentioned user", inline=False)

        modembed.set_thumbnail(url=self.client.user.avatar_url)


        ownerembed=discord.Embed(title=f"`cogs.OwnerCommands` Help", url="https://bit.ly/3gSAaJO", description="**Tip:** Don't try them, they don't work unless you are the owner of the bot :/", color=ctx.author.color, timestamp=ctx.message.created_at)

        ownerembed.add_field(name=f"`{ctx.prefix}add <amount of xp, @user (optional)>`", value="Adds xp to the targeted user (or yourself)", inline=False)
        ownerembed.add_field(name=f"`{ctx.prefix}reload <cog name (without cog.)>`", value="Reloads a cog instead of restarting bot", inline=False)
        ownerembed.add_field(name=f"`{ctx.prefix}reset <@user (optional)>`", value="Resets the users' level and exp stats", inline=False)

        ownerembed.set_thumbnail(url=self.client.user.avatar_url)

        if type == 'commands':
            await ctx.send(embed=commandsembed)
        elif type == 'coms':
            await ctx.send(embed=commandsembed)
        elif type == 'maincmds':
            await ctx.send(embed=commandsembed)
        
        elif type == 'fun':
            await ctx.send(embed=funembed)
        elif type == 'funcoms':
            await ctx.send(embed=funembed)
        elif type == 'funcmds':
            await ctx.send(embed=funembed)

        elif type == 'levelling':
            await ctx.send(embed=levelembed)
        elif type == 'level':
            await ctx.send(embed=levelembed)
        elif type == 'lvl':
            await ctx.send(embed=levelembed)
    
        elif type in 'moderation':
            await ctx.send(embed=modembed)
        elif type in 'mod':
            await ctx.send(embed=modembed)
        elif type in 'modtools':
            await ctx.send(embed=modembed)
        elif type == 'ownercmds':
            await ctx.send(embed=ownerembed)
        elif type == 'owner':
            await ctx.send(embed=ownerembed)
        elif type == 'ownercommands':
            await ctx.send(embed=ownerembed)

    @assistance.error
    async def assistance_error(self, ctx, error):
        embed=discord.Embed(title=f"Help Command", url="https://bit.ly/3gSAaJO", description="Helps guide you through the bot", color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.add_field(name="Commands", value=f"`{ctx.prefix}help commands`", inline=True)
        embed.add_field(name="Fun Commands", value=f"`{ctx.prefix}help fun`", inline=True)
        embed.add_field(name="Levelling", value=f"`{ctx.prefix}help levelling`", inline=True)
        embed.add_field(name="Moderation", value=f"`{ctx.prefix}help moderation`", inline=True)
        embed.add_field(name="oWnEr CoMmAnDs", value=f"`{ctx.prefix}help ownercmds`", inline=True)
        embed.add_field(name=f"**Alternate `types` (new feature) `{ctx.prefix}help <types>`:**", value="__Commands__ - coms, maincmds\n__Fun__ - funcmds, funcoms\n__Levelling__* - lvl, level\n__Moderation__ - mod, modtools\n__Ownercmds__ - owner, ownercommands", inline=False)

        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"⛔ Error! Surely you won't be missing permissions for the `{ctx.prefix}help` command...")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"⛔ Error! You are missing the `type` argument. Fill it in with the type of help you need!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"⛔ Error! `type` argument has to be a string!")

def setup(client):
    client.add_cog(HelpCmds(client))