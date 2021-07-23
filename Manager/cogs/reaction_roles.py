import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import json

class ReactionRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.reaction_roles = []

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        for role_id, msg, emoji in self.client.reaction_roles:
            if msg.id == payload.message_id and emoji == payload.emoji.name:
                if payload.member.bot == False:
                    guild = self.client.get_guild(int(payload.guild_id))
                    role = guild.get_role(role_id)
                    await payload.member.add_roles(role)
                    await payload.member.send(f'**ROLE ADDED:** You were given role `{role}` in server `{guild}`')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        for role_id, msg, emoji in self.client.reaction_roles:
            if msg.id == payload.message_id and emoji == payload.emoji.name:
                guild = self.client.get_guild(int(payload.guild_id))
                member = guild.get_member(payload.user_id)
                role = guild.get_role(role_id)
                await member.remove_roles(role)
                await member.send(f"**ROLE REMOVED:** Your role `{role}` was removed in server `{guild}`")

    @commands.command(aliases=['rroles'])
    @commands.has_permissions(manage_messages=True)
    async def reactionroles(self, ctx, msg: discord.Message=None, emoji=None, *, role: discord.Role=None):
        await msg.add_reaction(emoji)
        role_id = role.id
        self.client.reaction_roles.append((role_id, msg, emoji))
        await ctx.send(f'**REACTION ROLES: ** You have set message `{msg.content}` to a reaction roles message.\nEvery `{emoji}` added to the bot will give the user `{role}` role', delete_after=10.0)

    @reactionroles.error
    async def rroles_error(self, ctx, error):
        embed=discord.Embed(title=f"`{ctx.prefix}reactionroles` Usage", description=f"Use `{ctx.prefix}reactionroles <message id (integer), emoji (emoji), role name (string)>`\n\n**Examples:**\n`{ctx.prefix}reactionroles 123456789123456789 ✅ Member>`\n`{ctx.prefix}reactionroles 694206969696969 🤣 test cool cool`",color=0xFF0000)
        embed.set_author(name="How to get Message ID? (click me)", url="https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-")
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed multiple arguments. Check above ^ for more details')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! Arguments have to be the `type` mentioned above!\n**Tip:** Right click on the message you wanna add to, then click Copy ID. Paste that `message id`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⛔ Error! You lack the permission `Manage Messages`!')  

def setup(client):
    client.add_cog(ReactionRoles(client))