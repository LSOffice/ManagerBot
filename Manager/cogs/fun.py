import discord
import random
import asyncio
from discord.ext import commands

class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['rolladice'])
    async def dice(self, ctx, number: int):
        message = await ctx.send('Rolling...')
        await asyncio.sleep(1)
        if number >= 69420:
            await message.edit(content=f"{ctx.author.mention}, seems like your number is over or equal to `69420`. This is going to take a bit of time...")
            await asyncio.sleep(10)
        percentage = round(100/int(number))
        percentage = "<1" if percentage == 0 else percentage 
        await message.edit(content=f"{ctx.author.mention}, your dice rolled a **{random.randint(1, int(number))}**! ({percentage}%)")

    @dice.error
    async def dice_error(self, ctx, error):
        embed = discord.Embed(title=f"`{ctx.prefix}dice` Usage", description=f"Use `{ctx.prefix}dice <amount of sides>`\n\n**Examples:**\n`{ctx.prefix}dice 6`\n`{ctx.prefix}dice 12`",color=0xFF0000)
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⛔ Error! You have missed the `number` of the dice sides!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('⛔ Error! `number` argument has to be an `integer`!\n**Tip:** Try `an integer` for the `number` argument')

    @commands.command(aliases=['flipacoin', 'coin'])
    async def coinflip(self, ctx):
        message = await ctx.send('Flipping...')
        number = int(random.randint(1, 2))
        if number == 1:
            value = 'heads'
        elif number == 2:
            value = 'tails'
        await asyncio.sleep(1)
        await message.edit(content=f"{ctx.author.mention}, your coin flipped a **{value}**! (50%)")

def setup(client):
    client.add_cog(FunCommands(client))