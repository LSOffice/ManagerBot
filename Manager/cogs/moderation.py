import discord
from discord.ext import commands
from discord.utils import get
from log.logger import Log
import time
import asyncio

class ModTools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['boot'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="You have been kicked"):
        await member.kick(reason=reason)
        embed = discord.Embed(description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}", color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member} was kicked", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
        await member.send(f"You were kicked from `{ctx.guild.name}` by **{ctx.author}**\n**Reason:** {reason}")
        Log("audit", user=ctx.author, guild=ctx.author.guild.id, auditaction='kick', affecteduser=member)

    @kick.error
    async def kick_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}kick` Usage", description=f"Use `{ctx.prefix}kick <member>`\n\n**Examples:**\n`{ctx.prefix}kick @LSOffice`\n`{ctx.prefix}kick @Manager`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to kick!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Kick Members`!')

    @commands.command(pass_context=True, aliases=['foreverboot'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="You have been banned"):
        await member.ban(reason=reason)
        embed = discord.Embed(description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}", color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member} was banned", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
        await member.send(f"You were banned from `{ctx.guild.name}` by **{ctx.author}**\n**Reason:** {reason}")
        Log("audit", user=ctx.author, guild=ctx.author.guild.id, auditaction='ban', affecteduser=member)

    @ban.error
    async def ban_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}ban` Usage", description=f"Use `{ctx.prefix}ban <member>`\n\n**Examples:**\n`{ctx.prefix}ban @LSOffice`\n`{ctx.prefix}ban @Manager`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to ban!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Ban Members`!')

    @commands.command(pass_context=True, aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, type, amount: int):
        await asyncio.sleep(1)
        if type == 'all':
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"`{amount}` messages were deleted in `{ctx.channel}`", delete_after=2.0)
        elif type == 'image':
            await ctx.message.delete()
            await ctx.channel.purge(check=lambda m: m.attachments != [])
            await ctx.send(f"`{amount}` images were deleted in `{ctx.channel}`", delete_after=2.0)
        elif type == 'embed':
            await ctx.message.delete()
            await ctx.channel.purge(check=lambda m: m.embeds != [])
            await ctx.send(f"`{amount}` embeds were deleted in `{ctx.channel}`", delete_after=2.0)
    
    @clear.error
    async def clear_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}clear` Usage", description=f"Use `{ctx.prefix}clear <type, amount>`\n\n**Examples:**\n`{ctx.prefix}clear all 5`\n`{ctx.prefix}clear image 69`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        await ctx.send('**TIP:** If a message is more than 14 days old, you may not be able to delete it!')
        await ctx.send("**TIP:** If a type of message doesn't exist in that channel, you may not be able to delete it!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `amount` and `type` of lines and type you want to clear!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `amount` argument has to be an `integer`!')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')

    @commands.command(pass_context=True, aliases=['purgemass'])
    @commands.has_permissions(manage_messages=True)
    async def clearmass(self, ctx, times: int):
        await ctx.send('Clearing channel...')
        await asyncio.sleep(1)
        time = 0
        while time != int(times):
            await ctx.channel.purge(limit=100)
            await asyncio.sleep(.25)
            time += 1
        await asyncio.sleep(1)
        await ctx.send(f"`{times*100}` messages were deleted in `{ctx.channel}`", delete_after=2.0)

    @clearmass.error
    async def clearmass_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}clearmass` Usage", description=f"Use `{ctx.prefix}clearmass <times (this will x100)>`\n\n**Examples:**\n`{ctx.prefix}clearmass 5`\n`{ctx.prefix}clearmass 69`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        await ctx.send('**TIP:** If a message is more than 14 days old, you may not be able to delete it!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `amount` of times (x100) you want to clear!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `amount` argument has to be an `integer`!')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')

    @commands.command(pass_context=True, aliases=['alert'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason="You have been warned!"):
        embed = discord.Embed(description=f"**Reason:** {reason}", color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member} has been warned", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
        await member.send(f"You were warned in `{ctx.guild.name}` by **{ctx.author}**\n**Reason:** {reason}")

    @warn.error
    async def warn_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}warn` Usage", description=f"Use `{ctx.prefix}warn <@User, reason (optional)>`\n\n**Examples:**\n`{ctx.prefix}warn @LSOffice`\n`{ctx.prefix}warn @LSOffice testing`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to warn!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Kick Members`!')

    @commands.command(pass_context=True, aliases=['nospeak'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason="You have been muted."):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
                embed = discord.Embed(description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}", color=member.color, timestamp=ctx.message.created_at)
                embed.set_author(name=f"{member} was muted", icon_url=member.avatar_url)
                await ctx.send(embed=embed)
                return
            
                overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True, read_message_history=True)
                newRole = await guild.create_role(name="Muted")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole, overwrite=overwrite)

                await ctx.send(f'**ROLE CREATED:** Muted Role was created by {ctx.author.mention}')
                await member.add_roles(newRole)
                embed = discord.Embed(description=f"**Reason:** {reason}\n**By:** {ctx.author.mention}", color=member.color, timestamp=ctx.message.created_at)
                embed.set_author(name=f"{member.mention} was muted", icon_url=member.avatar_url)
                await member.send(f"You were muted in `{ctx.guild.name}` by **{ctx.author}**\n**Reason:** {reason}")
                await ctx.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}mute` Usage", description=f"Use `{ctx.prefix}mute <@User, reason>`\n\n**Examples:**\n`{ctx.prefix}mute @LSOffice testing`\n`{ctx.prefix}mute @Manager testing`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to mute!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')  

    @commands.command(pass_context=True, aliases=['speaknow'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        muted = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(muted)
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member} was unmuted", icon_url=member.avatar_url)
        await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}unmute` Usage", description=f"Use `{ctx.prefix}unmute <@User>`\n\n**Examples:**\n`{ctx.prefix}unmute @LSOffice`\n`{ctx.prefix}unmute @Manager`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to unmute!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `mention`!\n**Tip:** Try `@member` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')  

    @commands.command(pass_context=True, aliases=['nomoreboot'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(description=f"**By:** {ctx.author.mention}", color=user.color, timestamp=ctx.message.created_at)
                embed.set_author(name=f"{user} was unbanned", icon_url=user.avatar_url)
                await ctx.send(embed=embed)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}unban` Usage", description=f"Use `{ctx.prefix}unban <User>`\n\n**Examples:**\n`{ctx.prefix}unban LSOffice#3471`\n`{ctx.prefix}unban Manager#9300`",color=0xFF0000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `member` you want to unmute!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `member` argument has to be an `tag`!\n**Tip:** Try `User#1234` for the `member` argument')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Ban Members`!')

def setup(client):
    client.add_cog(ModTools(client))