import discord
from discord.ext import commands
from log.logger import Log
import time

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot ready')
        Log(status="bot_status", message="Ready")
        time.sleep(1)
        print('Logged in as:')
        print(f'{self.client.user}')
        channel = self.client.get_channel(750684069683134524)
        embed = discord.Embed(title='Bot Update', color=0x00ff08)
        embed.add_field(name="**Status**", value="Ready", inline=True)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_disconnect(self):
        print('Bot disconnected')
        Log(status="bot_status", message="Disconnected")
        channel = self.client.get_channel(750684069683134524)
        embed = discord.Embed(title='Bot Update', color=0xff0000)
        embed.add_field(name="**Status**", value="Disconnected", inline=True)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if isinstance(error, commands.MissingPermissions):
                await ctx.send('⛔ Error! You lack the permissions to do this!')
                Log(status='error', user=f'{ctx.message.author}', errono=1)
            elif isinstance(error, commands.NotOwner):
                await ctx.send(f'⛔ Error! You are not the owner of this bot: [`{self.client.user}`]')
            elif isinstance(error, commands.CheckFailure):
                await ctx.send('⛔ Error! Check failure, try again!')
                Log(status='error', user=ctx.author, errono=5)
            elif isinstance(error, commands.CommandNotFound):
                await ctx.send('⛔ Error! Invalid command/Command not found!')
            else:
                pass
        except Exception as e:
            raise e

def setup(client):
    client.add_cog(Events(client))