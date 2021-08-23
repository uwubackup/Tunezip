import discord
from discord.ext import commands

import aiohttp
from random import choice, randint

class quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def compliment(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            member = ctx.author

        compliments = [
            "Your positivity is infectious.",
            "You should be so proud of yourself.",
            "You’re amazing!",
            "You’re a true gift to the people in your life.",
            "You’re an incredible friend.",
            "I really appreciate everything that you do.",
            "You inspire me to be a better person.",
            "Your passion always motivates me.",
            "Your smile makes me smile.",
            "Thank you for being such a great person.",
            "The way you carry yourself is truly admirable.",
            "You are such a good listener.",
            "You have a remarkable sense of humor.",
            "Thanks for being you!",
            "You set a great example for everyone around you.",
            "I love your perspective on life.",
            "Being around you makes everything better.",
            "You always know the right thing to say.",
            "The world would be a better place if more people were like you!",
            "You are one of a kind.",
            "You make me want to be the best version of myself.",
            "You always have the best ideas.",
            "I’m so lucky to have you in my life.",
            "Your capacity for generosity knows no bounds.",
            "I wish I were more like you.",
            "You are so strong.",
            "I’ve never met someone as kind as you are.",
            "You have such a great heart.",
            "Simply knowing you has made me a better person.",
            "You are beautiful inside and out.",
        ]
        await ctx.send(
            embed=discord.Embed(
                description=f"{member.mention} {choice(compliments)}",
                colour = ctx.author.colour
            ).set_footer(text=f"From {ctx.author}")
        )

    @commands.command()
    async def quote(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animu/quote') as r:
                embed = discord.Embed(title= "Quotes", description = "Get random anime quotes", colour = ctx.author.colour)
                embed.add_field(name="Quote:", value=(await r.json())['sentence'], inline = False)
                embed.add_field(name="Said by:", value=(await r.json())['characther'], inline = True)
                embed.add_field(name="In:", value=(await r.json())['anime'], inline = True)
                await ctx.send(embed =embed)

    @commands.command()
    async def catfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/cat') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def dogfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/dog') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def pandafact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/panda') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def birdfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/bird') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def foxfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/fox') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def koalafact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/koala') as r:
                await ctx.send((await r.json())['fact'])

def setup(bot):
    bot.add_cog(quotes(bot))